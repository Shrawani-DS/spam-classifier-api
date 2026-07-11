import streamlit as st
import requests

st.title("📩 Spam Classifier")
st.info("First request may take ~1 min (free hosting)")

text = st.text_area("Enter email text")

if st.button("Predict"):
    url = "https://spam-classifier-api-xv9i.onrender.com"
    
    response = requests.post(
    url + "/predict",
    json={"message": text}
)
    
    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
    else:
        st.error("Error in prediction")