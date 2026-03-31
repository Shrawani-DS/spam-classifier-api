from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model and vectorizer
model = joblib.load(open("model/spam_model.pkl", "rb"))
tfidf_vectorizer = joblib.load(open("model/tfidf.pkl", "rb"))

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
    
    # Transform text
    vectorized_text = tfidf_vectorizer.transform([text])
    
    # Predict
    prediction = model.predict(vectorized_text)[0]
    probability = model.predict_proba(vectorized_text)[0][1]
    
    return {
        "message": text,
        "prediction": "Spam" if prediction == 1 else "Not Spam",
        "spam_probability": float(probability)
    }