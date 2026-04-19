
# 💳 Financial Fraud Detection System

## 📌 Overview

This project is a **Machine Learning-based Financial Fraud Detection System** that identifies whether a transaction is **fraudulent or legitimate**.

The model is trained on a credit card transaction dataset using advanced data preprocessing and classification techniques. A **Flask web application** is built to allow users to input transaction details and get real-time predictions.

---

## 🚀 Features

* 🔍 Detects fraudulent transactions using ML
* 📊 Trained on real-world credit card dataset
* ⚡ Fast predictions using trained model
* 🌐 Web interface using Flask
* 🧠 Handles 29 input features (V1–V28 + Amount)
* 📈 High accuracy model

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Flask**
* **HTML (Frontend)**

---

## 📂 Project Structure

```
fraud_detection/
│
├── templates/
│   └── index.html
│
├── app.py
├── model.pkl
├── creditcard_2023.csv
└── README.md
```

---

## ⚙️ How It Works

1. User enters transaction details (29 features)
2. Data is sent to Flask backend
3. Model processes the input
4. Prediction is generated:

   * ✅ Normal Transaction
   * ⚠️ Fraud Transaction

---

## ▶️ Run Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/fraud-detection.git
cd fraud-detection
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Model Details

* Algorithm: (e.g., Logistic Regression / Random Forest)
* Input Features: 29
* Output: Binary Classification (Fraud / Normal)
* Evaluation Metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-Score

---

## 📸 Screenshots

![Home Page](images.jpg)


---

## 🎯 Future Improvements

* 📂 CSV file upload for bulk prediction
* 🎨 Improved UI/UX design
* 🌐 Deploy on cloud (Render / Railway)
* 🔐 Add authentication system

---

## 👨‍💻 Author

**Ganesh Kumar**

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
