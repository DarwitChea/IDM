import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('IDM.csv')
missing_values = df.isnull().sum()

# Box Plot
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['Age'])
plt.title("Box Plot of Age")
plt.show()

# Scatter plot
# plt.figure(figsize=(10, 5))
# sns.scatterplot(x=df['Age'], y=df['No'])
# plt.title("Scatter Plot of Age vs.No")
# plt.xlabel("Age")
# plt.ylabel("No")
# plt.show()
