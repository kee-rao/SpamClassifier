# Spam Classifier Flask App

This is a simple Flask web application to classify messages as **Spam** or **Not Spam** using an ML model trained using LogisticRegression

## Features

- Clean and preprocess input text.
- Uses a Logistic Regression spam classifier (`spam_classifierLR.pkl`).
- Shows prediction result with confidence score.
- Simple, user-friendly web interface.

## Requirements

- Python 3.7+
- Flask
- scikit-learn
- joblib

## Setup

1. Clone this repository or copy the files to your project directory.

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
    ```bash
    python app.py
    ```
