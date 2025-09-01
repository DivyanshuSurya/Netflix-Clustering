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