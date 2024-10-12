import pandas as pd

df = pd.read_csv('IDM.csv')
missing_values = df.isnull().sum()
print(missing_values)
