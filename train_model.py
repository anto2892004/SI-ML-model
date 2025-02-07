import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("crop_data.csv")  # Ensure you have a dataset

X = data.drop(columns=['label'])  # Features
y = data['label']  # Target variable (crop name)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("crop_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
