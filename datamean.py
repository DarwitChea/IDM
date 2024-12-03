import numpy as np

regular_data = np.array([10, 20, 30, 40, 50])
print(f'Mean of regular data: {regular_data.mean()}')

outlier_data = np.array([10, 20, 30, 40, 500])
print(f'Mean of data with an outlier: {outlier_data.mean()}')
