# 🏭 Industrial Vision Ops: End-to-End Anomaly Detection

## 🎯 Project Overview

This repository implements a production-oriented MLOps pipeline for industrial visual quality control using the MVTec AD dataset.
The system detects surface defects (e.g., scratches, dents, contamination) using two complementary approaches:
- Scikit-learn baseline (Isolation Forest on engineered features)
- PyTorch deep learning model (Autoencoder-based anomaly detection)

Beyond modeling, the project focuses on reproducibility and deployment, including:

- 📊 Experiment tracking with **MLflow**
- 🐳 Containerization with **Docker**
- ☸️ Deployment on **Kubernetes (Minikube)**
- 🔁 Continuous delivery via **GitOps (ArgoCD + Helm)**

The result is a fully reproducible pipeline that goes from `data ingestion → training → evaluation → API inference → Kubernetes deployment`.
