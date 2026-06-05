import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("customer_churn_model.pkl")

st.title("📊 Customer Churn Prediction")

st.sidebar.header("Customer Details")

# Numeric Features
age = st.sidebar.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

days_since_last_login = st.sidebar.number_input(
    "Days Since Last Login",
    min_value=0,
    value=5
)

customer_service_calls = st.sidebar.number_input(
    "Customer Service Calls",
    min_value=0,
    value=1
)

monthly_spend = st.sidebar.number_input(
    "Monthly Spend ($)",
    min_value=0.0,
    value=100.0
)

# Encoded Features
gender_non_binary = st.sidebar.selectbox(
    "Gender",
    ["No", "Yes"]
)

region_south = st.sidebar.selectbox(
    "Region South",
    ["No", "Yes"]
)

subscription_plan_plus = st.sidebar.selectbox(
    "Subscription Plan Plus",
    ["No", "Yes"]
)

payment_method_paypal = st.sidebar.selectbox(
    "Payment Method PayPal",
    ["No", "Yes"]
)

if st.button("Predict Churn"):

    input_data = pd.DataFrame({
        'Age': [age],
        'Days_Since_Last_Login': [days_since_last_login],
        'Customer_Service_Calls': [customer_service_calls],
        'Monthly_Spend': [monthly_spend],
        'Gender_Non-Binary': [1 if gender_non_binary == "Yes" else 0],
        'Region_South': [1 if region_south == "Yes" else 0],
        'Subscription_Plan_Plus': [1 if subscription_plan_plus == "Yes" else 0],
        'Payment_Method_PayPal': [1 if payment_method_paypal == "Yes" else 0]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("❌ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")

    # Probability (if supported by model)
    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(input_data)[0][1]
        st.write(f"Churn Probability: **{prob:.2%}**")