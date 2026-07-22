import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Email Spam Classifier",
    page_icon="📩",
    layout="centered"
)

# Title
st.title("📩 Email Spam Classifier")

st.write(
    "Enter the email or SMS message below to determine whether it is **Spam** or **Ham**."
)

st.info("⏳ First request may take about a minute because the backend is hosted on a free server.")

# User input
text = st.text_area(
    "Enter your message",
    height=180,
    placeholder="Type or paste your email/SMS here..."
)

# Predict button
if st.button("Predict"):

    if text.strip() == "":
        st.warning("Please enter a message.")
    else:

        url = "https://spam-classifier-api-xv9i.onrender.com"

        try:
            response = requests.post(
                url + "/predict",
                json={"message": text},
                timeout=60
            )

            if response.status_code == 200:

                result = response.json()

                if result["prediction"] == "Spam":
                    st.error("🚨 Prediction: SPAM")
                else:
                    st.success("✅ Prediction: HAM")

            else:
                st.error("Prediction failed. Please try again.")

        except requests.exceptions.RequestException:
            st.error("Unable to connect to the prediction API.")