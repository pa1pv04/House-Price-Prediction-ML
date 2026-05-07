import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib

# Load dataset
df = pd.read_csv("Housing.csv")

# Convert yes/no to 1/0
binary_cols = [
    'mainroad',
    'guestroom',
    'basement',
    'hotwaterheating',
    'airconditioning',
    'prefarea'
]

for col in binary_cols:
    df[col] = df[col].map({'yes': 1, 'no': 0})

# Convert furnishingstatus manually
df['furnishingstatus'] = df['furnishingstatus'].map({
    'furnished': 2,
    'semi-furnished': 1,
    'unfurnished': 0
})

# Features
X = df.drop('price', axis=1)

# Target
y = df['price']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(n_estimators=100)

# Train
model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)

accuracy = r2_score(y_test, predictions)

print("Accuracy:", round(accuracy * 100, 2), "%")

# Save model
joblib.dump(model, "model.pkl")

print("Model Saved")