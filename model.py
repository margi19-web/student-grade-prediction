import pandas as pd 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
data = pd.read_csv("student-mat.csv", sep=";")

features = ["G1", "G2", "studytime", "absences", "failures", "age"]

X = data[features]
y = data["G3"]

print("Input variables:")
print(X.head())

print("\nTarget variable (G3):")
print(y.head())

print("\nNumber of input features:", X.shape[1])
print("Number of students:", X.shape[0])
from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))
from sklearn.linear_model import LinearRegression

# Create the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel training completed!")
# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel evaluation:")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R²:", round(r2, 2))
import joblib

# Save the trained model
joblib.dump(model, "student_grade_model.pkl")

print("\nModel saved successfully!")
