# 🚚 AI-Powered Delivery Delay Prediction & Optimization System

A Machine Learning-based system to predict whether a delivery will be delayed using logistics, order, and weather data. The project focuses on building a robust predictive model and deploying it via a Streamlit application.

---

## 📌 Project Overview

This project analyzes large-scale supply chain data and predicts **late delivery risk (0 = On Time, 1 = Delayed)** using advanced machine learning techniques. It enables proactive logistics planning and helps improve operational efficiency.

---

## ⚙️ Features

- ✅ Predicts delivery delay risk
- 📊 Provides delay probability score
- ⚡ Uses ensemble models (Random Forest)
- 🔍 Feature engineering using:
  - Time-based patterns (weekday, month)
  - Weather conditions (precipitation, windspeed, severity)
  - Shipping and order behavior
- 🖥️ Interactive UI built with Streamlit

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn 
- **Visualization:** Matplotlib, Seaborn  
- **Deployment:** Streamlit, Docker  

---

## 🧠 Machine Learning Pipeline

### 1. Data Preprocessing
- Handling missing values  
- Removing data leakage  
- Dropping high-cardinality and irrelevant features  
- Encoding categorical variables  

### 2. Feature Engineering
- Time-based features (weekday, month)  
- Weather impact features  
- Shipping behavior features  

### 3. Model Training
- Random Forest   

### 4. Evaluation
- Accuracy, Precision, Recall, F1-score  

---

## 📁 Project Structure
project/
│
├── app.py # Streamlit app
├── main.py # Data pre processing 
├── delivery_model.pkl # Trained ML model 
├── columns.pkl # Training feature columns
├── requirements.txt
├── README.md


---

## ⚠️ Important Notes

- The **trained model file (`delivery_model.pkl`) is included** for predictions.
- The **feature structure file (`columns.pkl`) ensures correct input format during prediction**.
- The **main training file (`main.py`) is large and not uploaded to GitHub**.
- It is available inside the **Docker environment** for execution.

---

## 🐳 Docker Support

The complete project (including training pipeline) is available via Docker.
https://hub.docker.com/repository/docker/prajwal25xd/deliverydateestimator/general

### Run using Docker:
```bash
docker pull prajwal25xd/deliverydateestimator
docker run -p 8501:8501 prajwal25xd/deliverydateestimator
