import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load your traffic data (assuming it’s in CSV format)
data = pd.read_csv('traffic-data.csv')  # Update with your actual path
print(data.head())

# Assuming the traffic data has a column 'Traffic' with the number of requests per minute
X = data[['Traffic']].values

# Initialize and fit the Isolation Forest model
model = IsolationForest(contamination=0.05)  # Adjust contamination level as needed
model.fit(X)

# Predict anomalies (-1 for anomaly, 1 for normal)
data['Anomaly'] = model.predict(X)
anomalies = data[data['Anomaly'] == -1]

# Print detected anomalies
print("Anomalies detected:")
print(anomalies)

import matplotlib.pyplot as plt

# Plot the traffic data and anomalies
plt.figure(figsize=(10, 6))
plt.plot(data['Traffic'], label='Traffic Data')
plt.scatter(anomalies.index, anomalies['Traffic'], color='red', label='Anomalies')
plt.xlabel('Time')
plt.ylabel('Traffic')
plt.legend()
plt.savefig('anomalies_plot.png')  # Save plot as image
