import pandas as pd
from sklearn.ensemble import IsolationForest

# Load dataset
data = pd.read_csv("data.csv")

# Select features
features = data[['amount', 'transactions', 'age']]

# Train model
model = IsolationForest(contamination=0.05)
data['fraud'] = model.fit_predict(features)

# Convert output
data['fraud'] = data['fraud'].map({1: 0, -1: 1})

# Save output
data.to_csv("output.csv", index=False)

print("Fraud Detection Completed!")
print(data)