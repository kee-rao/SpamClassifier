# Spam Classifier Flask App

A lightweight Flask web application that classifies emails as **Spam** or **Not Spam** using a pre-trained Logistic Regression model. Ideal for detecting unwanted messages quickly and accurately.

---

## 🚀 Features

- 🧹 **Text Cleaning & Preprocessing**: Normalizes input text (lowercasing, tokenization, stopword removal, etc.).
- 🤖 **Machine Learning Model**: Uses a trained `LogisticRegression` model (`spam_classifierLR.pkl`) for predictions.
- 📊 **Confidence Scoring**: Displays probability confidence alongside the classification.
- 🖥️ **Web Interface**: User-friendly form to enter email text and receive real-time results.

---
## Requirements

- Python 3.7+
- Flask
- scikit-learn
- joblib
---
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
---
