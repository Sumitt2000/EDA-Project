import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
df = pd.read_csv("INDUSTRY.csv")
print(df.head())
print(df.shape)
print(df.describe())
print(df.dtypes)
df['created_date'] = pd.to_datetime(df['created_date'])
print(df.isnull().sum())
print(df.duplicated().sum())
sns.histplot(df['annual_revenue_million'],kde=True)
plt.show()
sns.boxplot(x=df['annual_revenue_million'])
plt.show()
df['industry'].value_counts()
df['industry'].value_counts().plot(kind='bar')
plt.show()
corr = df.corr(numeric_only=True)
print(corr)
plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

sns.scatterplot(
    x='employee_count',
    y='annual_revenue_million',
    hue='industry',
    data=df
)
plt.show()
sns.barplot(
    x='region',
    y='profit_margin_percent',
    data=df
)
plt.show()
sns.scatterplot(
    x='market_rating',
    y = 'profit_margin_percent',
    data=df
)
plt.show()
from scipy.stats import zscore 
z_scores = zscore(df['annual_revenue_million'])
print(z_scores)

