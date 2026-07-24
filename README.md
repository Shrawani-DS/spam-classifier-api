# 📧 Email Spam Classification using NLP | FastAPI | Streamlit | Docker

## 📌 Project Overview

Email spam is one of the most common cybersecurity and productivity challenges. This project presents an end-to-end Machine Learning solution that classifies emails as **Spam** or **Not Spam** using Natural Language Processing (NLP).

The application uses **TF-IDF Vectorization** and a **Multinomial Naive Bayes** classifier to analyze email text. The trained model is served using **FastAPI**, integrated with a **Streamlit** frontend for user interaction, and containerized using **Docker** for easy deployment.

---

## 🎯 Problem Statement

The objective of this project is to build a machine learning model capable of automatically identifying spam emails, reducing the need for manual filtering while improving communication security and user productivity.

---

## 🚀 Features

- Email Spam Prediction
- NLP Text Preprocessing
- TF-IDF Feature Extraction
- Multinomial Naive Bayes Classifier
- REST API using FastAPI
- Interactive Streamlit Web Interface
- Dockerized Application
- Cloud Deployment Ready

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Natural Language Processing
- TF-IDF Vectorizer

### API
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### Deployment
- Docker
- Render

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```text
Email_Spam_Classifier/
│
├── app/
│   ├── main.py
│   ├── preprocessing.py
│   └── __init__.py
│
├── model/
│   ├── linear_svm_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebook/
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## 🏗️ Project Workflow

```text
Email
   │
   ▼
Text Preprocessing
   │
   ▼
TF-IDF Vectorization
   │
   ▼
Multinomial Naive Bayes
   │
   ▼
FastAPI REST API
   │
   ▼
Streamlit UI
   │
   ▼
Spam / Not Spam
```

---

## 🤖 Machine Learning Model

| Component | Details |
|-----------|---------|
| Feature Extraction | TF-IDF Vectorizer |
| Algorithm | Multinomial Naive Bayes |
| Problem Type | Binary Classification |

---

## ⚙️ Run Locally

### Clone Repository

```bash
git clone <repository-url>
cd Email_Spam_Classifier
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI

```bash
python -m uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

### Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

## 🐳 Docker

Build Docker Image

```bash
docker build -t spam-api .
```

Run Container

```bash
docker run -p 8000:8000 spam-api
```

---

## 📷 Application Screenshots

### Streamlit UI



### FastAPI Swagger Documentation


### Prediction Result


---

## 🔮 Future Improvements

- Compare multiple ML algorithms
- Hyperparameter tuning
- Deep Learning (LSTM/BERT)
- Email attachment analysis
- Multilingual spam detection
- CI/CD pipeline
- AWS Deployment

---

## 👩‍💻 Author

**Shrawani Deshpande**

Electrical Engineer transitioning into Data Science with hands-on experience in Machine Learning, NLP, FastAPI, Docker, SQL, and AWS.

Feel free to connect and explore my projects!
