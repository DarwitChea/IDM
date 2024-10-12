import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('IDM.csv')
missing_values = df.isnull().sum()

sns.bplot(x=df['Age'])
plt.show()
