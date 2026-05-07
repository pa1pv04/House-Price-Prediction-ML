# House Price Prediction using Machine Learning

This project is a Machine Learning based web application designed to predict house prices based on various property features such as area, number of bedrooms, bathrooms, stories, parking availability, furnishing status, and other amenities.

The application uses a Random Forest Regression model trained on a housing dataset to provide accurate price predictions. Users can enter property details through a simple and interactive web interface, and the system instantly predicts the estimated house price.

## Features
- Predicts house prices in real time
- User-friendly web interface built with Flask
- Data preprocessing and feature encoding
- Machine Learning model training and evaluation
- Model saving and loading using Joblib

## Tech Stack
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML

## Project Structure

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

## Installation & Setup
1. Clone the repo
```bash
git clone YOUR_GITHUB_LINK

Install Required Libraries
pip install -r requirements.txt

3. Train the Model
python train_model.py

4. Run the Flask Application
python app.py

5. Open in Browser
http://127.0.0.1:5000

Machine Learning Model
Random Forest Regressor

Author
Pavan Kumar Balla
