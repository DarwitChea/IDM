import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('IDM.csv')
valid_age_data = df[(df['Age'] >= 1) & (df['Age'] <= 80)]

plt.figure(figsize=(10, 6))
plt.hist(valid_age_data['Age'], bins=50, color='skyblue', edgecolor='black')
plt.title('Histogram of Age (1 to 80)')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

outliers = df[df['Age'] > 80]
if not outliers.empty:
    print(f"Outlier(s) detected: \n{outliers}")
