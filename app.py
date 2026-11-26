import pandas as pd
import joblib

# 1. Load the trained machine learning model
model = joblib.load("student_grade_model.pkl")

print("Student Grade Prediction System")
print("Model loaded successfully!")
# Get student information from the user


def get_number(prompt, minimum, maximum, integer=False):
    while True:
        try:
            value = float(input(prompt))

            if integer and not value.is_integer():
                print("Please enter a whole number.")
                continue

            if minimum <= value <= maximum:
                return int(value) if integer else value

            print(f"Please enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input. Please enter a number.")
print("\nPlease enter the student's information:")

g1 = get_number("First period grade (G1):", 0, 20)
g2 = get_number("Second period grade (G2):", 0, 20)
studytime = get_number("Weekly study time (1-4): ", 1, 4, integer= True)
absences = get_number("Number of absences (0-93): ", 0, 93, integer=True) 
failures = get_number("Number of past class failures: ", 0, 4, integer= True)
age = get_number("Student age: ", 15, 22, integer=True )

# Organize the input data for the model
student_data = pd.DataFrame([{
    "G1": g1,
    "G2": g2,
    "studytime": studytime,
    "absences": absences,
    "failures": failures,
    "age": age
}])

# Predict the final grade
predicted_grade = model.predict(student_data)[0]

# Display the prediction
print("\n" + "=" * 40)
print("        STUDENT GRADE REPORT")
print("=" * 40)

print(f"Predicted final grade: {predicted_grade:.2f} / 20")

if predicted_grade >= 10:
    print("Status: PASS!")
else:
    print("Status: BELOW PASSING GRADE :(")

print("=" * 40)
predicted_grade = max(0, min(20, predicted_grade))
