Seaborn
-----

```python
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
sns.set(color_codes=True)
%matplotlib inline 
%config InlineBackend.figure_format = 'svg'
```

```python
fig, ax = plt.subplots()
fig.set_size_inches(15, 8)

g = sns.heatmap(data_kosmo.corr(),cmap='coolwarm',annot=False,linecolor='white',linewidths=1)

labels = g.get_xticklabels() # получить список заголоаков
g.set_xticklabels(labels, rotation=75); # подпись с пворотом
```

**Barplot** - график с колонками

```python
from numpy import median
ax1 = fig.add_subplot(141)

sns.barplot(x='prediction', y='round_type_1', data=tips, ax=ax1, estimator=median)
```

Добавим расстояние между картинками

```python
gs = fig.add_gridspec(1, 5,wspace=0.4)
ax1 = fig.add_subplot(gs[0,0])
sns.barplot(x='prediction', y='total_cards_done', data=data_kosmo, ax=ax1, estimator=median)
```

- Распределение: `sns.distplot(data["reg_day_type"],kde=False);`
- Два на один график: `sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter');`
- Показать все отношения: `sns.pairplot(tips);`