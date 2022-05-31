```python
data = pd.read_csv("user_features.csv",index_col="id")
res = pd.read_csv("predictions.csv",index_col="id") 

df = pd.DataFrame(data={"user_id":df_test.index.values,
                       "prediction":model.predict(df_test)})

data_kosmo = pd.concat([data, res], axis=1, sort=False) # axis=1 - по индексу

df.to_csv("mypredictions.csv",index=False)
df.head()

```

Merge to one excel doc
--------------------------------
```python
from pyexcel import merge_all_to_a_book

merge_all_to_a_book(['Export Products Sheet.csv', 'Export Groups Sheet.csv'], "output.xlsx")
```


Clear style
--------------------------------
```python
import openpyxl
wb = openpyxl.load_workbook("output.xlsx")
for sheet in wb:
    sheet_name = sheet.title
    sheet.title = sheet_name.replace(".csv", "")
    print(sheet_name)
wb.save("output.xlsx")
```