from sklearn.ensemble import IsolationForest
import pandas as pd

df = pd.read_csv('data/network_traffic.csv')
features = df[['Length']]  

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(features)

df['anomaly'] = model.predict(features)

df.to_csv('data/network_traffic_with_anomalies.csv', index=False)
anomalies = df[df['anomaly'] == -1]
print(f"Detected {len(anomalies)} anomalies")
