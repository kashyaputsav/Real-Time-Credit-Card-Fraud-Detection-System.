# 💳 Real-Time Credit Card Fraud Detection System

## 📌 Overview
A scalable, production-ready machine learning system for detecting fraudulent credit card transactions in real time.  
The project focuses on handling extreme class imbalance, optimizing precision-recall tradeoffs, and providing model explainability for decision transparency.

---

## 🎯 Problem Statement
Credit card fraud detection presents key challenges:
- Highly **imbalanced datasets** (fraud cases are rare)
- Need for **low-latency predictions** in real-time systems
- Requirement for **interpretable models** in financial applications

This system addresses these challenges using a robust ML pipeline and API-based deployment.

---

## 🧠 Solution Architecture

```
Raw Data → Preprocessing → SMOTE → Model Training (XGBoost)
         → Hyperparameter Tuning (Optuna)
         → Evaluation (Precision-Recall Optimization)
         → Explainability (SHAP)
         → Deployment (FastAPI)
```

---

## 📊 Performance

| Metric     | Score |
|------------|------|
| Precision  | 93%  |
| Recall     | 85%  |

- Optimized using **precision-recall tradeoff**
- Focused on minimizing **false positives** while maintaining strong recall

---

## ⚙️ Key Features

- **Imbalance Handling**
  - SMOTE-based oversampling for minority class

- **Model Optimization**
  - Hyperparameter tuning using Optuna

- **Explainability**
  - SHAP for feature-level prediction insights

- **Real-Time Inference**
  - FastAPI-based REST API for low-latency predictions

- **Production-Oriented Design**
  - Modular code structure
  - Model serialization using joblib

---

## 🛠 Tech Stack

- **Languages:** Python  
- **ML:** XGBoost, Scikit-learn  
- **Data:** Pandas, NumPy  
- **Imbalance Handling:** imbalanced-learn (SMOTE)  
- **Optimization:** Optuna  
- **Explainability:** SHAP  
- **Backend:** FastAPI  
- **Serving:** Uvicorn  

---

## 📂 Project Structure

```
.
├── api/
│   └── app.py              # FastAPI application
├── models/
│   └── model.pkl          # Trained model
├── src/                   # Core ML pipeline
├── notebooks/             # Experiments and analysis
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone Repository
```
git clone <your-repo-url>
cd fraud-detection
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run the API Server
```
uvicorn api.app:app --reload
```

---

## 🔌 API Usage

### Endpoint
```
POST /predict
```

### Sample Request
```json
{
  "features": [0.1, -1.2, 3.4, ...]
}
```

### Sample Response
```json
{
  "fraud": true,
  "probability": 0.92
}
```

---

## 📈 Model Explainability

- Uses **SHAP (SHapley Additive Explanations)**
- Provides per-transaction feature importance
- Enables:
  - Debugging model predictions
  - Auditability for financial systems

---

## 🧪 Future Improvements

- Real-time streaming (Kafka / Flink)
- Model monitoring and drift detection
- Docker containerization
- Kubernetes deployment
- Feature store integration
- CI/CD pipelines

---

## 👨‍💻 Author
Utsav Kashyap
