import streamlit as st
import matplotlib.pyplot as plt

def plot_price_distribution(df):
    """Plots the price change distribution."""
    st.subheader("Price Change Distribution")
    plt.figure(figsize=(10, 5))
    plt.hist(df['Price_Change'].dropna(), bins=50, edgecolor='black')
    plt.xlabel("Price Change (%)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Price Changes")
    st.pyplot(plt)
