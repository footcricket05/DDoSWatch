import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Load your traffic data (assuming it's in CSV format)
data = pd.read_csv(r"C:\Users\SHAURYA\OneDrive\Desktop\SEM 8 Subjects\DDoSWatch\data\traffic-data.csv")  # Update with your actual path
print(data.head())

# Assuming the traffic data has a column 'Traffic' with the number of requests per minute
X = data[['Traffic']].values

# Assuming you have a 'True_Label' column where 1 = normal, -1 = attack (DDoS)
y_true = data['True_Label']  # Update with your actual column name for true labels

# Initialize and fit the Isolation Forest model
model = IsolationForest(contamination=0.05)  # Adjust contamination level as needed
model.fit(X)

# Predict anomalies (-1 for anomaly, 1 for normal)
data['Anomaly'] = model.predict(X)
anomalies = data[data['Anomaly'] == -1]

# Print detected anomalies
print("Anomalies detected:")
print(anomalies)

# Compare predictions with true labels to calculate accuracy
accuracy = accuracy_score(y_true, data['Anomaly'])
print(f"Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix
conf_matrix = confusion_matrix(y_true, data['Anomaly'])
print("Confusion Matrix:")
print(conf_matrix)

# Precision, Recall, F1 Score
print("Classification Report:")
print(classification_report(y_true, data['Anomaly']))

# Plot the traffic data and anomalies
plt.figure(figsize=(10, 6))
plt.plot(data['Traffic'], label='Traffic Data')
plt.scatter(anomalies.index, anomalies['Traffic'], color='red', label='Anomalies')
plt.xlabel('Time')
plt.ylabel('Traffic')
plt.legend()
plt.savefig('anomalies_plot.png')  # Save plot as image
