This project is an end-to-end Machine Learning application that classifies emails as Spam or Not Spam using TF-IDF vectorization and Naive Bayes algorithm, deployed via FastAPI and containerized using Docker.
Tech Stack: 
            Python
            Scikit-learn
            TF-IDF Vectorizer
            Naive Bayes
            FastAPI
            Docker
How to run locally:
uvicorn app.main:app --reload

Open:
http://localhost:8000/docs

Run Using Docker:
docker build -t spam-api . 
docker run -p 8000:8000 spam-api

Model Details:
Vectorization: TF-IDF
Algorithm: Multinomial Naive Bayes
