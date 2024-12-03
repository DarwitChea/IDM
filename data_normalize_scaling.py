# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

# Let's create a simple dataframe
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [100, 200, 400, 800, 1000],
    'C': [200, 400, 600, 800, 1000]
})

# Initialize a min-max scaler
min_max_scaler = MinMaxScaler()
# Scale the dataframe
df_min_max = pd.DataFrame(min_max_scaler.fit_transform(df), columns=df.columns)

# Initialize a standard scaler
std_scaler = StandardScaler()
# Scale the dataframe
df_std = pd.DataFrame(std_scaler.fit_transform(df), columns=df.columns)

# Initialize a robust scaler
robust_scaler = RobustScaler()
# Scale the dataframe
df_robust = pd.DataFrame(robust_scaler.fit_transform(df), columns=df.columns)

# Print the original and scaled data
print("Original Data")
print(df)

print("\nMin-Max Scaled Data")
print(df_min_max)

print("\nStandard Scaled Data")
print(df_std)

print("\nRobust Scaled Data")
print(df_robust)
