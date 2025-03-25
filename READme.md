✈️ Airline Customer Satisfaction Prediction

🔥 Project Overview

This project predicts customer satisfaction levels for airlines based on multiple factors such as age, class,Customer_Type,Type_of_Travel,flight distance, delays, and service quality etc. The project consists of:
✅ FastAPI Backend - Serves the machine learning model for predictions.
✅ Streamlit Frontend - User-friendly UI for entering customer details.
✅ Dockerized Deployment - Containerized using Docker for easy deployment.
✅ GitHub Actions CI/CD - Runs tests and deploys images to Docker Hub.

📌 Table of Contents

Demo

Tech Stack

Installation

Usage

Project Structure

Docker Deployment

Testing

License


🚀 Demo

🔹 FastAPI Docs: http://127.0.0.1:4000/docs
🔹 Streamlit UI: http://localhost:8501

🛠 Tech Stack

Machine Learning: Scikit-Learn, Pandas, Joblib

Backend API: FastAPI, Uvicorn

Frontend UI: Streamlit

Containerization: Docker, Docker Compose

CI/CD: GitHub Actions

Testing: Pytest, Requests

🔧 Installation

1️⃣ Clone the Repository

git clone 
git clone https://github.com/ka1817/Predicting-Airline-Customer-Satisfaction-Using-Machine-Learning.git
cd Predicting-Airline-Customer-Satisfaction-Using-Machine-Learning

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

🎯 Usage

1️⃣ Run the FastAPI Backend

uvicorn main:app --host 0.0.0.0 --port 4000
🔹 API Documentation: Visit http://127.0.0.1:4000/docs

2️⃣ Run the Streamlit Frontend

streamlit run app.py
🔹 Access the UI: http://localhost:8501

📁 Project Structure

📦 airline-customer-satisfaction
 ┣ 📂 .github                    # GitHub Actions workflows (CI/CD)
 ┃ ┗ 📜 deploy.yml               # Deployment pipeline
 ┣ 📂 Data                       # Raw and processed data
 ┣ 📂 mlartifacts                # ML artifacts (like feature importance, logs)
 ┣ 📂 mlruns                     # MLflow experiment tracking
 ┣ 📂 models                     # Trained ML models
 ┣ 📂 Research                   # Notebooks, research files
 ┣ 📂 test                       # Unit and integration tests
 ┣ 📂 venv                       # Virtual environment (not included in repo)
 ┣ 📜 .dockerignore              # Ignore unnecessary files for Docker builds
 ┣ 📜 .gitignore                 # Ignore unnecessary files for Git
 ┣ 📜 app.py                     # Streamlit frontend
 ┣ 📜 backend.Dockerfile         # Dockerfile for FastAPI backend
 ┣ 📜 docker-compose.yml         # Docker Compose config
 ┣ 📜 frontend.Dockerfile        # Dockerfile for Streamlit frontend
 ┣ 📜 main.py                    # FastAPI backend
 ┣ 📜 predictions.py             # Prediction logic script
 ┣ 📜 README.md                  # Project documentation
 ┗ 📜 requirements.txt           # Dependencies

🐳 Docker Deployment
1️⃣ Build and Run the Containers

docker-compose up --build
🔹 Backend: http://localhost:4000
🔹 Frontend: http://localhost:8501

2️⃣ Pull the Images from Docker Hub

docker pull pranavreddy123/airline-backend
docker pull pranavreddy123/airline-frontend
docker-compose up

✅ Testing
Run tests using pytest:
pytest test/


📜 License
This project is open-source and available under the MIT License.









