

### Oversampling
```python
from imblearn.over_sampling import SMOTE

sm = SMOTE(random_state = 2)
X, y = sm.fit_sample(X_train, y_train.ravel())
```

### Normalizer
```python
from sklearn.preprocessing import Normalizer
X = Normalizer().fit_transform(X)
```

### Split Data
```python
from sklearn.model_selection import train_test_split

X_train, X_validation, y_train, y_validation = train_test_split(X, y,
                                                                train_size=0.85, random_state=7)
```

###  GridSearch
```python
from sklearn.model_selection import GridSearchCV
from catboost import CatBoostClassifier

model = CatBoostClassifier()

parametrs = { 'iterations': range(400, 900, 50),
              'depth': range(3,7, 1),}

grid = GridSearchCV(model, parametrs, cv=5)
grid.fit(X_train, y_train, verbose=0)
grid.best_params_
```

### Catboost
```python
model = CatBoostClassifier(
    thread_count=4,
    iterations=850,
    depth=6,
    learning_rate = 0.01,
    sampling_frequency = "PerTreeLevel",
    nan_mode = "Forbidden",
    custom_metric = ['Logloss', 'AUC', 'F1'],
    use_best_model=True
)
model.fit(
    X_train, y_train,
    eval_set=(X_validation, y_validation),
    logging_level='Silent',
    plot=True
)
```
### Plot feature_importances_
```
import matplotlib.pyplot as plt
sns.set(style="darkgrid")

fig = plt.figure()
fig.set_size_inches(16, 4)

plt.bar(np.arange(len(model.feature_importances_)),model.feature_importances_)
plt.xticks(np.arange(len(model.feature_importances_)), model.feature_names_,rotation=70);
```

### F1 - score
```python
from sklearn import metrics

y_pred = [model.predict(x) for x in X_validation.values]
print(metrics.classification_report(y_validation, y_pred,
                                    digits=3))
```