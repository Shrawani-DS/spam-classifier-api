from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from app.preprocessing import transform_text


# Load model and vectorizer
model = joblib.load(r"model\linear_svm_model.pkl")
tfidf_vectorizer = joblib.load(r"model\tfidf_vectorizer.pkl")

app = FastAPI(title="Spam Email Classifier API")

# Request schema
class EmailRequest(BaseModel):
    message: str

# Root endpoint
@app.get("/")
def home():
    return {"message": "Spam Classifier API is running"}

# Prediction endpoint
@app.post("/predict")
def predict_spam(data: EmailRequest):
    text = data.message

    processed_text = transform_text(text)
    vectorized_text = tfidf_vectorizer.transform([processed_text])

    prediction = model.predict(vectorized_text)[0]

    return {
        "message": text,
        "prediction": "Spam" if prediction == 1 else "Ham"
    }