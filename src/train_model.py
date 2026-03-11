import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("data/student_depression.csv")

# Normalize column names
data.columns = (
    data.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("Columns in dataset:")
print(data.columns)

# Select useful columns
features = [
    "age",
    "gender",
    "sleep_duration",
    "academic_pressure",
    "work_pressure",
    "work/study_hours",
    "financial_stress",
    "dietary_habits",
    "family_history_of_mental_illness",
    "depression"
]

data = data[features]

# Remove missing values
data = data.dropna()

# Encode categorical columns
encoder = LabelEncoder()

for col in data.columns:
    if data[col].dtype == "object":
        data[col] = encoder.fit_transform(data[col])

# Split features and target
X = data.drop("depression", axis=1)
y = data["depression"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save features
with open("model/features.pkl", "wb") as f:
    pickle.dump(X.columns.tolist(), f)

print("Model trained successfully")
print("Features used:", X.columns.tolist())