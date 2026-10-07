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

Dataset

The project uses the Jigsaw Toxic Comment dataset.

The comment_text column is used as the input text and the toxic column is used as the target label.

0 = Non-toxic
1 = Toxic

The dataset contains 159,571 comments.

The dataset is not uploaded to this repository because of its size and is excluded using .gitignore.

Model
TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts text into numerical features that can be processed by the machine learning model.

The implementation uses:

Maximum features: 50,000
Unigrams and bigrams
Logistic Regression

Logistic Regression is used as the text classification algorithm to predict whether a comment is potentially harmful.

Model Performance

The model was evaluated on a separate test set.

Metric	Score
Accuracy	95.63%
Precision	92.54%
Recall	59.17%
F1 Score	72.18%

Because the dataset is imbalanced, precision, recall, and F1 score are also considered when evaluating the model.

Example
Cyberbullying Detection System
1. Check Message
2. Exit

Enter your choice: 1
Enter a message: You are a stupid loser.

Result: Potentially Harmful
Action: Harmful content detected.
Action: Content removed.
Remediated Message: [Content removed due to harmful language]

## Demo

![Project Demo](demo.png)


Project Structure
Cyberbullying-Detection-and-Remediation/
│
├── cyberbullying_detector.py
├── train_model.py
├── README.md
└── .gitignore


How to Run
1. Install required libraries
pip install pandas scikit-learn joblib
2. Train the model
python train_model.py

This creates the trained model and TF-IDF vectorizer locally.

3. Run the application
python cyberbullying_detector.py
Remediation

When potentially harmful content is detected, the application performs a simulated remediation action by replacing the message with:

[Content removed due to harmful language]

This is only a simulation and does not connect to or modify any real social-media platform.

Limitations
The model is trained on toxic-comment labels rather than a dataset specifically labeled for cyberbullying.
The model may produce false positives or false negatives.
It is a text-classification prototype and does not understand all forms of context, sarcasm, or indirect harassment.
The remediation action is simulated.
No real social-media platform integration is included.
Future Improvements
Improve recall for harmful content
Experiment with other machine learning models
Use a dataset specifically focused on cyberbullying
Add a web-based user interface
Add confidence scores
Improve text preprocessing
Add more advanced NLP techniques


## Note

This is an educational machine learning prototype inspired by the concept of cyberbullying detection and remediation.
