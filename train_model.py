import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  # Use RandomForestClassifier for classification tasks
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset (Update the filename to the correct dataset you're using)
data = pd.read_csv('Seed_Classification_Dataset.csv')  # Replace with actual file path

# Data preprocessing (modify this based on your dataset)
# Assuming features such as 'Length', 'Width', 'Perimeter', 'Area', 'Compactness', and 'Class'
# Ensure there are no missing values or handle them if needed

# Prepare feature and target variables
X = data[['Length', 'Width', 'Perimeter', 'Area', 'Compactness']]  # Features
y = data['Class']  # Target variable (Seed classification labels)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)  # Change to RandomForestClassifier
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# More detailed classification report (precision, recall, F1-score)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the model to a file
joblib.dump(model, 'seed_classifier_model.pkl')
print("Model saved as seed_classifier_model.pkl")
