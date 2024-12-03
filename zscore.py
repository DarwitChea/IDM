import numpy as np
from scipy import stats

# Sample data
data = np.array([20000, 1, 2, 2, 3, 4, 5, 6, 100,
                101, 1000, 2000, 3000, 10000])

# Calculate the z-scores
z_scores = np.abs(stats.zscore(data))

# Identify outliers with a threshold (e.g., z-score > 3)
outliers = data[z_scores > 2]

print("Z-Score Outliers:", outliers)


Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

# Determine the outlier range
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = data[(data < lower_bound) | (data > upper_bound)]
print("IQR Outliers:", outliers)
