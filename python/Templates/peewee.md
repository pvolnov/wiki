Class
---
```python
class PredictingUnit(Model):
    user_id = IntegerField(index=True, null=False)
    valid = BooleanField(default=True)
    last_modified = DateTimeField(default="SWL")

    name = TextField(default="No name")
    cover = TextField(default="")

    purpose_type = TextField(default="")
    goods_type = ArrayField(TextField, default=[])
    categories = JSONField(default={})
    group = IntegerField(default=-1)

    liked = ArrayField(IntegerField, default=[])
    incard = ArrayField(IntegerField, default=[])
    disliked = ArrayField(IntegerField, default=[])
    total_marked = IntegerField(default=0)
    mean_price = IntegerField(default=800)

    liked_keywords = JSONField(default={})
    disliked_keywords = JSONField(default={})
    predict_items = ArrayField(IntegerField, default=[])

    class Meta:
        database = db
        db_table = 'PredictingUnit'
```


Update postgress
---
```python
IkeaItems.insert_many(on_rep[k:k + 100]).on_conflict(conflict_target=[IkeaItems.code],
                                                              update={IkeaItems.search: EXCLUDED.search,
                                                                      IkeaItems.name: EXCLUDED.name,})
     
```