# Cyberbullying Detection and Remediation

A Python-based machine learning project for detecting potentially harmful online content and applying a simulated remediation action.

The project uses TF-IDF text vectorization and Logistic Regression to classify text as either Safe or Potentially Harmful.

## Features

- Accepts user messages through a command-line interface
- Converts text into numerical features using TF-IDF
- Uses Logistic Regression for text classification
- Classifies messages as Safe or Potentially Harmful
- Handles empty input
- Applies simulated content removal for harmful messages
- Provides an interactive menu
- Supports repeated message checking

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Joblib
- Git and GitHub

## Machine Learning Pipeline

```text
Text Dataset
     ↓
Train/Test Split
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression
     ↓
Model Evaluation
     ↓
Saved ML Model
     ↓
New User Message
     ↓
Prediction
     ↓
Safe / Potentially Harmful
     ↓
Simulated Remediation
