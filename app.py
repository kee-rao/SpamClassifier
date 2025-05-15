from flask import Flask, render_template, request
import joblib
import re

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("spam_classifierLR.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r"[.,/]", "", text)
        return text.lower()
    return ""

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None

    if request.method == "POST":
        message = request.form["message"]
        cleaned = clean_text(message)
        transformed = vectorizer.transform([cleaned])
        pred = model.predict(transformed)[0]
        proba = model.predict_proba(transformed)[0]

        prediction = "Spam" if pred == 1 else "Not Spam"
        confidence = f"{max(proba) * 100:.2f}% confident"

    return render_template("index.html", prediction=prediction, confidence=confidence)


if __name__ == "__main__":
    app.run(debug=True)
