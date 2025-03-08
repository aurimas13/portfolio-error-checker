import streamlit as st
import pandas as pd
from src.data_loader import load_data
from src.error_detector import detect_errors
from src.ai_analyzer import ai_detect_anomalies
from src.visualization import plot_price_distribution

# Load and process data
df = load_data()
df = detect_errors(df)
df = ai_detect_anomalies(df)

# Streamlit UI
st.title("📊 Portfolio Error Detection Dashboard")
st.dataframe(df[df['Price_Change_Anomaly'] | df['Missing_Trade_Info'] | df['Weight_Anomaly_Flag'] | df['Trade_Price_Issue'] | df['AI_Detected_Anomaly']])

plot_price_distribution(df)

st.subheader("🔍 Detected Anomalies")
st.dataframe(df[df['AI_Detected_Anomaly'] == True])
