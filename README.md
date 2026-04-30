# MediStock AI

**Intelligent Medicine Demand Forecasting and Safe Inventory Recommendation System**

##  Overview

MediStock AI is an end-to-end machine learning project designed to help hospitals and pharmacies forecast medicine demand and maintain safe stock levels.

Instead of relying on average sales, this system predicts next-day demand using historical daily sales data and provides:

* **predicted demand**
* **uncertainty range**
* **recommended stock level**
* **risk indicator**
* **interactive dashboard visualization**

This helps reduce **shortages** and **medicine wastage**.

---

##  Problem Statement

Hospitals and pharmacies often use average demand for stock planning, which may lead to:

* medicine shortages
* overstocking
* expiry losses
* emergency procurement costs

This project solves that by using machine learning-based forecasting with decision support.

---

##  Features

*  Daily medicine demand forecasting
*  Uncertainty-aware prediction range
*  Safe stock recommendation
*  Risk level classification
*  FastAPI backend API
*  React dashboard frontend
*  Visual charts for demand trends

---

##  Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

### Backend

* FastAPI
* Uvicorn

### Frontend

* React (Vite)
* Axios
* Recharts

### Development

* Google Colab
* Antigravity / VS Code

---

##  Dataset

The model is trained on **daily medicine sales data** for a single drug.

### Features Used

* day
* month
* day_of_week
* is_weekend
* lag_1
* lag_7
* rolling_mean_7
* quarter
* day_of_year
* rolling_std_7

### Target

* demand

---

##  Model

The forecasting model uses:

**Random Forest Regressor**

This was chosen because it performs well on tabular time-based feature engineering tasks.

---

##  Uncertainty Logic

To improve decision-making, the system provides a confidence range using a simple ±15% buffer.

Example:

Prediction = 100
Range = 85 – 115

Recommended stock = upper bound

This ensures safer stock planning.

---

##  API Response Example

```json
{
  "prediction": 103.4,
  "lower": 87.89,
  "upper": 118.91,
  "recommended_stock": 119,
  "risk": "medium",
  "insight": "Maintain buffer stock"
}
```

---

##  Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Install dependencies:

```bash
pip install fastapi uvicorn pandas scikit-learn joblib
```

Run server:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

##  Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Run React app:

```bash
npm run dev
```

Open:

```text
http://localhost:5173
```

---

##  Project Workflow

```text
Daily sales dataset
↓
data cleaning
↓
feature engineering
↓
model training
↓
save .pkl model
↓
FastAPI backend
↓
React dashboard
↓
prediction + stock recommendation
```
