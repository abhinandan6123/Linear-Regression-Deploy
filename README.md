
# 📊 Linear Regression ML Deployment

This repository demonstrates an **end-to-end Machine Learning workflow**, covering **model training, serialization, API creation, version control, and cloud deployment**.

The project is based on a Linear Regression demo tutorial, adapted to modern tools and platform constraints.

---

## 🚀 Project Overview

The goal of this project is to:

* Train a **Linear Regression model**
* Serve predictions using a **Flask web API**
* Version-control the project using **Git & GitHub**
* Deploy the application as a **live cloud service**

🔗 **Live Application URL**
👉 [https://linear-regression-deploy-5158.onrender.com](https://linear-regression-deploy-5158.onrender.com)

---

## 🧠 Dataset Used

### ❌ Original (Video Tutorial)

* Boston Housing Dataset (`load_boston`)
* Removed from scikit-learn due to ethical and compatibility issues

### ✅ Actual Implementation

* **California Housing Dataset** (`fetch_california_housing`)
* Officially supported by scikit-learn
* Suitable for regression problems

This change preserves the learning objective while ensuring **modern library compatibility**.

---

## 🛠️ Technologies Used

* **Python**
* **Libraries**

  * NumPy
  * Pandas
  * Scikit-learn
  * Flask
  * Gunicorn
* **IDE**: VS Code + Jupyter Notebook
* **Version Control**: Git, GitHub
* **Deployment Platform**: Render (Python Web Service)

---

## ⚙️ Project Structure

```
Linear_Regression_Deploy/
│
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version specification
├── linear_regression_model.pkl # Trained ML model
├── scaler.pkl                  # Feature scaler
├── templates/                  # HTML templates (if used)
├── .gitignore
└── README.md
```

---

## 🔄 Workflow

1. **Data Loading**

   * California Housing dataset loaded using scikit-learn

2. **Preprocessing**

   * Train-test split
   * Feature scaling using StandardScaler

3. **Model Training**

   * Linear Regression model trained using scikit-learn

4. **Model Serialization**

   * Model and scaler saved using `pickle`

5. **API Development**

   * Flask app created with `/predict` endpoint
   * JSON input → numerical prediction output

6. **Version Control**

   * Git repository initialized
   * Code pushed to GitHub

7. **Deployment**

   * Deployed as a **Python Web Service** on Render
   * Gunicorn used as production WSGI server

---

## 🌐 Deployment Details

* **Platform**: Render
* **Service Type**: Web Service (not Static Site)
* **Build Command**

  ```
  pip install -r requirements.txt
  ```
* **Start Command**

  ```
  gunicorn app:app
  ```

Docker and Heroku were not used due to:

* Platform restrictions
* Credit card requirements
* OS compatibility issues

---

## ⚠️ Known Warning (Expected Behavior)

During deployment, the following warning appears:

```
InconsistentVersionWarning (scikit-learn)
```

### Explanation:

* Model was trained using an older scikit-learn version
* Deployment environment uses a newer version
* The model loads and predicts correctly

This is a **documented and non-fatal warning**.

---

## 🔁 Comparison with Reference Tutorial

| Feature          | Video Tutorial | This Project       |
| ---------------- | -------------- | ------------------ |
| Dataset          | Boston Housing | California Housing |
| Deployment       | Heroku         | Render             |
| Docker           | Used           | Not Used           |
| GitHub Actions   | Used           | Not Used           |
| Cost             | Paid           | Free               |
| OS Compatibility | Limited        | Windows Friendly   |

---

## ✅ Final Outcome

* ✔ Model trained successfully
* ✔ API responding correctly
* ✔ GitHub repository maintained
* ✔ Cloud deployment completed
* ✔ Public live URL generated

---

## 🧾 One-Line Project Summary

> A Linear Regression model was trained using the California Housing dataset, serialized with pickle, exposed through a Flask API, version-controlled using GitHub, and deployed as a live cloud web service on Render.

---

## 📌 Future Enhancements (Optional)

* Add HTML UI for user input
* Improve error handling
* Add API documentation (Swagger)
* Add CI/CD pipeline

---

🎥 Reference & Credits

This project was inspired by and initially guided through a demo tutorial by Krish Naik, a well-known Data Scientist and ML educator.

YouTube Channel: Krish Naik

Reference Video:
https://www.youtube.com/watch?v=Gs15V79cauo

Note

The original tutorial used:

Boston Housing Dataset

Heroku & Docker-based deployment

Due to:

Deprecation of the Boston dataset

Heroku’s paid-only policy

Platform and OS constraints

the implementation was adapted and modernized using:

California Housing Dataset

Render Cloud Platform

Direct GitHub integration (without Docker)

The core learning objectives and ML workflow remain the same, while ensuring compatibility with current tools and libraries.
