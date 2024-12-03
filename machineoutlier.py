import numpy as np
from sklearn.ensemble import IsolationForest

# Sample data
outlier_data = np.array([1, 2, 2, 3, 4, 5, 6, 100, 101])

# Initialize the Isolation Forest model
clf = IsolationForest(contamination=0.2)

# Fit the model
clf.fit(outlier_data.reshape(-1, 1))

# Predict the outliers
pred = clf.predict(outlier_data.reshape(-1, 1))

# Outliers are marked with a -1
outliers = outlier_data[pred == -1]

print("Outliers:", outliers)
