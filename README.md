# Stock Price Prediction MLOps Project

## 📌 Overview
This project demonstrates an **end-to-end MLOps pipeline** for predicting stock prices from the Indian market.  
It integrates modern tools like **Airflow, MLflow, DVC, FastAPI, Docker, Jenkins/GitHub Actions, SonarQube, Trivy, and ArgoCD**.

The pipeline:
1. Ingests stock data (Yahoo Finance / NSE).
2. Cleans and preprocesses the data.
3. Generates technical indicators (moving averages, returns).
4. Trains a machine learning model and saves it as `.pkl`.
5. Automates workflow with Airflow.
6. Tracks experiments with MLflow.
7. Containerizes the prediction API with Docker.
8. Deploys via ArgoCD.

---

## 🏗️ Project Structure

stock-mlops/
├── src/                  # Core scripts
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   └── train_model.py
├── dags/                 # Airflow DAGs
│   └── stock_pipeline_dag.py
├── models/               # Saved models
│   └── saved_model.pkl
├── docker/               # Containerization
│   ├── Dockerfile
│   └── requirements.txt
├── mlflow_tracking/      # MLflow setup
├── tests/                # Unit tests
└── README.md
