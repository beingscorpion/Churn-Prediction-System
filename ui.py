# ui.py
import streamlit as st
import pandas as pd

def get_user_input():
    st.subheader("📋 Customer Information")
    col1, col2 = st.columns(2)

    with col1:
        tenure = st.number_input("Customer Tenure (Months)", min_value=0, max_value=72, value=12)
        monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)

    with col2:
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
        senior_citizen = st.selectbox("Senior Citizen", [0, 1])

    user_df = pd.DataFrame({
        'tenure': [tenure],
        'MonthlyCharges': [monthly_charges],
        'InternetService': [internet_service],
        'Contract': [contract],
        'PaymentMethod': [payment_method],
        'SeniorCitizen': [senior_citizen]
    })

    return user_df
