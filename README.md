# Simple CI/CD Docker App  
A minimal FastAPI-based application demonstrating a complete **CI/CD pipeline** using **GitHub Actions**, **Docker**, automated tests, and code quality checks.  
This project is part of my DevOps portfolio and shows my understanding of modern DevOps workflows.

---

## 🚀 Project Overview
This repository contains a small FastAPI application packaged in a Docker container and built automatically using a CI pipeline.  

The CI workflow includes:

- 🔹 Code checkout  
- 🔹 Python setup  
- 🔹 Dependency installation  
- 🔹 Code linting with `flake8`  
- 🔹 Unit testing with `pytest`  
- 🔹 Docker image build  

No cloud account is required — the project runs fully locally and in GitHub Actions.

---

## 🛠️ Technologies Used
- **FastAPI** – lightweight Python web framework  
- **Docker** – containerization  
- **GitHub Actions** – CI/CD pipeline  
- **pytest** – unit testing  
- **flake8** – code style checking  
- **Python 3.10**  

---

## 📁 Project Structure
simple-ci-cd-docker-app/
│
├── app/
│ ├── main.py
│ └── requirements.txt
│
├── tests/
│ └── test_main.py
│
├── Dockerfile
├── .dockerignore
│
├── .github/
│ └── workflows/
│ └── ci.yml
│
└── README.md

---

## ▶️ Running the Application Locally

### 1. Install dependencies
pip install -r app/requirements.txt

### 2. Run the app
uvicorn app.main:app --reload

The application will start on:  
http://127.0.0.1:8000

---

## 🧪 Run Tests
pytest

---

## 🐳 Docker Instructions

### Build the Docker image
docker build -t simple-ci-cd-docker-app .

### Run the container
docker run -p 8000:8000 simple-ci-cd-docker-app

---

## 🔄 CI/CD Pipeline (GitHub Actions)
The workflow is located in:  
`.github/workflows/ci.yml`

Pipeline steps:

1. Checkout repository  
2. Install Python  
3. Install dependencies  
4. Linting (`flake8`)  
5. Unit tests (`pytest`)  
6. Docker build  

This demonstrates a real DevOps CI workflow suitable for production.

---

## 🎯 What This Project Demonstrates
- Ability to set up automated CI pipelines  
- Containerization of applications  
- Writing and running unit tests  
- Working with GitHub workflows  
- Clean project organization  
- DevOps best practices  

---

## 📌 Future Enhancements
- Add deployment job (Azure / AWS / Docker Hub)  
- Add code coverage  
- Add GitHub badges  
- Add CD pipeline when cloud account becomes available  

---

## 👩‍💻 Author
**Velyana Petrova**  
DevOps Engineer in training  

---