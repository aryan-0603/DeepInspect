from sklearn.ensemble import IsolationForest
import pandas as pd

# Load raw data
df = pd.read_csv('data/network_traffic.csv')
features = df[['Length']]  # Use packet length as the feature for anomaly detection

# Train Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(features)

# Predict anomalies (-1 = anomaly, 1 = normal)
df['anomaly'] = model.predict(features)

# Save results
df.to_csv('data/network_traffic_with_anomalies.csv', index=False)
anomalies = df[df['anomaly'] == -1]
print(f"Detected {len(anomalies)} anomalies")