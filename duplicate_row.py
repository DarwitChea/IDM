import pandas as pd

df = pd.read_csv('IDM.csv')

duplicate_rows = df.duplicated()
print(f"Number of duplicate rows: {duplicate_rows.sum()}")

df = df.drop_duplicates()
print("Dataframe after removing Duplicates: ", df.shape)
