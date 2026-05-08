#  House Price Prediction using Machine Learning

A Machine Learning based web application that predicts house prices based on various property features such as area, number of bedrooms, bathrooms, stories, parking availability, furnishing status, and other amenities.

The application uses a **Random Forest Regression** model trained on housing data to provide accurate price predictions through a simple and interactive web interface built with Flask.

---

##  Features

- Predicts house prices in real time
- User-friendly web interface using Flask
- Data preprocessing and feature encoding
- Machine Learning model training and evaluation
- Model saving and loading using Joblib
- Fast and interactive prediction system

---

##  Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- Joblib

---

##  Project Structure

```bash
House-Price-Prediction/
│
├── app.py
├── train_model.py
├── model.pkl
├── Housing.csv
├── README.md
│
└── templates/
    └── index.html
```

---

##  Installation & Setup

### 1️ Clone the Repository

```bash
git clone YOUR_GITHUB_LINK
```

---

### 2️ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 3️ Train the Model

```bash
python train_model.py
```

---

### 4 Run the Flask Application

```bash
python app.py
```

---

### 5️ Open in Browser

```text
http://127.0.0.1:5000
```

---

##  Machine Learning Model

This project uses:

### Random Forest Regressor

The model is trained on housing data to predict house prices based on user inputs and property features.

---

##  Input Features

The model predicts house prices using features like:

- Area
- Bedrooms
- Bathrooms
- Stories
- Parking
- Furnishing Status
- Main Road Access
- Air Conditioning
- Preferred Area
- Guest Room Availability

---

##  Learning Outcomes

Through this project, I learned:

- Machine Learning model training
- Regression algorithms
- Data preprocessing and encoding
- Building web applications using Flask
- Model deployment basics
- Handling user inputs in web forms
- Saving and loading ML models using Joblib

---

##  Future Improvements

- Improve UI design
- Deploy the application online
- Add more advanced prediction models
- Use larger real-world datasets
- Add data visualization dashboards

---

##  Author

**Pavan Kumar Balla**
