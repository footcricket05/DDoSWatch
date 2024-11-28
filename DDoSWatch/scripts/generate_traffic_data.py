import pandas as pd
import numpy as np

# Generate synthetic traffic data
np.random.seed(0)
data_points = 1440  # Number of data points (e.g., 1440 minutes in a day)
traffic_data = np.random.poisson(lam=50, size=data_points)  # Generate traffic counts with random noise

# Introduce some anomalies by adding unusually high values
anomaly_indices = np.random.choice(data_points, size=10, replace=False)
traffic_data[anomaly_indices] = traffic_data[anomaly_indices] * 5

# Create a DataFrame and save to CSV
data = pd.DataFrame({'Traffic': traffic_data})
data.to_csv('traffic-data.csv', index=False)

print("Synthetic traffic data saved to 'traffic-data.csv'")
