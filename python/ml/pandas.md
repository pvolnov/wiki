```python
data = pd.read_csv("user_features.csv",index_col="id")
res = pd.read_csv("predictions.csv",index_col="id") 

df = pd.DataFrame(data={"user_id":df_test.index.values,
                       "prediction":model.predict(df_test)})

data_kosmo = pd.concat([data, res], axis=1, sort=False) # axis=1 - по индексу

df.to_csv("mypredictions.csv",index=False)
df.head()

```