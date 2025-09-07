# IRIS FLOWER CLASSIFICATION

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Step 1: CSV load karte hain
data = pd.read_csv("Iris.csv")

print("Dataset loaded! First 5 rows:")
print(data.head())

# Step 2: Features and target
X = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = data['Species']

# Step 3: Labels ko numbers me convert karte hain
le = LabelEncoder()
y = le.fit_transform(y)
print("\nLabel mapping:", dict(zip(le.classes_, le.transform(le.classes_))))

# Step 4: Split data train aur test me
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Model create karte hain aur train karte hain
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 6: Accuracy check karte hain
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", acc)

# Step 7: Model save karte hain
joblib.dump(model, "iris_model.pkl")
print("Model saved as 'iris_model.pkl'")

# Step 8: Chhota sa demo prediction
sample = [[5.1, 3.5, 1.4, 0.2]]  # Example input
pred = model.predict(sample)
print("Demo prediction for", sample, "is", le.inverse_transform(pred)[0])
