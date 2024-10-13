import pandas as pd

df = pd.read_csv('IDM.csv')

df['Gender_formatted'] = df['Gender'].str.strip().str.lower()

print(df['Gender_formatted'])
