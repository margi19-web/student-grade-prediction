# Student Grade Prediction System 
## Prokect Overview
thi prokect is a machine learning application designed to predict students' final math grades and provid personalized study reccomendations. 
## Dataset 
The project uses the Student Performance Dataset from the UCI Machine Learning Repository. 
- Subject: Mathematics
- Number of students: 395
- Input features: 6
- Target variable: G3 (final grade)
- Grade scale: 0–20

Dataset source:
https://archive.ics.uci.edu/dataset/320/student+performance

## Machine Learning Model

The initial model used Linear Regression. With the assistance of GitHub Copilot, different algorithms were evaluated and Random Forest was selected based on its better cross-validation performance.

### Model Performance

| Metric | Linear Regression | Random Forest |
|---|---:|---:|
| R² | 0.7824 | 0.8537 |
| MAE | 1.3340 | 1.0459 |
| RMSE | 2.1124 | 1.7322 |

## Main Features

### 1. Student Grade Prediction

Predicts the student's final mathematics grade based on six input variables and displays the predicted passing status.

### 2. Personalized Study Recommendations

Provides study recommendations based on study time, school absences and previous academic failures.

### 3. What-if Study Simulator

Allows users to compare predicted grades under different study-time scenarios.

## Installation

Install the required Python libraries:

```bash
python3 -m pip install -r requirements.txt
```

## How to Run

Train and save the machine learning model:

```bash
python3 model.py
```

Start the application:

```bash
python3 app.py
```

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Visual Studio Code
- Git and GitHub
- GitHub Copilot

## Limitations

The predictions are statistical estimates and do not guarantee actual academic outcomes. The study simulator identifies statistical relationships rather than causal effects.

The model is based on a relatively small dataset, which may limit its generalizability.

## Educational Purpose

This project was developed as an academic assignment for the Data Science and AI course at Korea University.