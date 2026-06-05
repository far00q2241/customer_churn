# Customer Churn Prediction

## Project Overview

This project predicts whether a customer is likely to churn (leave the service) based on customer demographics, engagement metrics, subscription details, and payment information.

A machine learning classification model was trained using historical customer data and deployed using Streamlit.

## Features Used

* Age
* Days Since Last Login
* Customer Service Calls
* Monthly Spend
* Gender (Non-Binary)
* Region (South)
* Subscription Plan (Plus)
* Payment Method (PayPal)

## Target Variable

* **0** → Customer Stays
* **1** → Customer Churns

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

## Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
├── customer_churn_model.pkl
├── requirements.txt
├── README.md
└── dataset.csv
```

## Streamlit Application

The web application allows users to:

* Enter customer information
* Predict churn probability
* Identify customers at risk of leaving

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Example Prediction

Input:

* Age = 35
* Days Since Last Login = 10
* Customer Service Calls = 3
* Monthly Spend = $120

Output:

* Customer likely to Churn
* Churn Probability: 78%

## Future Improvements

* Hyperparameter tuning
* Feature engineering
* Advanced ensemble models
* Customer retention recommendations

## Author

Farooq Khan

Machine Learning Enthusiast | Data Science
