import collections
import json

from flask import Flask, request
from flask_cors import cross_origin
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)


class Objects(Model):
    ...


@app.route('/')
def hello_world():
    return 'Hello World!'


def get_tree(objects):
    def add_tids(array):
        if len(array) > 2:
            # print(array.replace("'", "\""))
            return json.loads(array.replace("'", "\"").replace("None", '"None"'))
        else:
            return []

    res = collections.defaultdict(list)
    for o in objects:
        res["Hierarchy"] += add_tids(o.Hierarchy)
        res["People"] += add_tids(o.People)
        res["Processes"] += add_tids(o.Processes)
        res["Practices"] += add_tids(o.Practices)
        res["Metrics"] += add_tids(o.Metrics)

    tids = []
    for v in res.values():
        tids += v

    return res, tids


@app.route('/get_options', methods=['GET'])
@cross_origin()
def get_options():
    objects = Objects.select(Objects.item_id, Objects.type, Objects.name).execute()

    options = collections.defaultdict(list)
    for o in objects:
        options[o.type].append({"text": o.name, "value": o.item_id})
    options = dict(options)
    del options[""]
    return options


@app.route('/set_filtrs', methods=['POST'])
@cross_origin()
def set_filtrs():
    objects = Objects.select(Objects.item_id, Objects.tid, Objects.type, Objects.name, Objects.Metrics,
                             Objects.Practices,
                             Objects.Processes, Objects.Hierarchy, Objects.People).where(
        Objects.item_id.in_(request.json['keys'])).execute()

    res, tids = get_tree(objects)

    objects2 = Objects.select(Objects.item_id, Objects.type, Objects.name, Objects.tid).where(
        Objects.tid.in_(tids)).execute()
    object_names = {o.tid: o.tid + " " + o.name for o in objects2}

    items = [o.type + ": " + o.name for o in objects]
    for key, value in res.items():
        items += [key + ": " + object_names[v] for v in value if v in object_names]
    print(items)

    return {"items": items}


from flask import send_file


@app.route('/download_file.xlsx', methods=['GET'])
@cross_origin()
def download_file():
    return send_file("output.xlsx", attachment_filename="result.xlsx")


@app.route('/get_file', methods=['POST'])
@cross_origin()
def get_file():
    import pandas as pd
    with pd.ExcelWriter('output.xlsx') as writer:
        for item_id in request.json['keys']:
            print(item_id)
            doc = Objects.get(Objects.item_id == item_id)
            res, tids = get_tree([doc])
            items = Objects.select().where(Objects.tid.in_(tids)).execute()
            items = {i.tid: model_to_dict(i) for i in items}

            for key, tids in res.items():
                pd.DataFrame.from_dict([items[tid] for tid in tids]).to_excel(writer, index=False,
                                                                              sheet_name=(str(doc.tid) + " " + str(
                                                                                  doc.name)[:20] + " " + key)[:31])

    return {"status": "ok"}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
