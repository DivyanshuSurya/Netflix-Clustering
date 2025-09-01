import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('mymoviedb.csv', lineterminator=
'\n')
df.head()
df.info()
df['Genre'].head()
df.duplicated().sum()
df.describe()
df.head()
df['Release_Date'] = pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtypes)
df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes
df.info()
df.head()
cols = ['Overview', 'Original_Language', 'Poster_Url']
df.drop(cols, axis = 1, inplace = True)
df.columns
df.head()
def categorize_col(df, col, labels):
    edges = [df[col].describe()['min'],
df[col].describe()['25%'],
df[col].describe()['50%'],
   df[col].describe()['75%'],
    df[col].describe()['max']]



labels = ['not_popular', 'below_avg', 'average', 'popular']
catigorize_col(df, 'Vote_Average', labels)
df['Vote_Average'].unique()
df['Vote_Average'].value_counts()
df.dropna(inplace = True)

df.isna().sum()
df.head()
df['Genre'] = df['Genre'].str.split(', ')

df = df.explode('Genre').reset_index(drop=True)
df.head()
df['Genre'] =df['Genre'].astype('category')

df['Genre'].dtypes
df.info()
df.nunique()
sns.set_style('whitegrid')
df['Genre'].describe()
sns.catplot(y = 'Genre', data = df, kind = 'count',
order = df['Genre'].value_counts().index,
color = '#4287f5')
plt.title('genre column distribution')
plt.show()
sns.catplot(y = 'Vote_Average', data = df, kind = 'count',
order = df['Vote_Average'].value_counts().index,
color = '#4287f5')
plt.title('votes destribution')
plt.show()
