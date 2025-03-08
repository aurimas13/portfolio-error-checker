def detect_errors(df):
    """Detects portfolio inconsistencies like price jumps, missing trades, and weight anomalies."""
    df['Price_Change'] = df.groupby('P_Ticker')['Price'].pct_change()
    df['Price_Change_Anomaly'] = df['Price_Change'].apply(lambda x: abs(x) > 0.3)
    
    df['Quantity_Change'] = df['Close Quantity'] - df['Open Quantity']
    df['Missing_Trade_Info'] = (df['Quantity_Change'] != 0) & (df['Price'].isnull())

    df['Weight_Anomaly'] = df['Closing Weights'] - df['Opening Weights']
    df['Weight_Anomaly_Flag'] = df['Weight_Anomaly'].apply(lambda x: abs(x) > 0.05)

    df['Trade_Price_Issue'] = (df['Price'] < 0) | (df['Price'].isnull())
    
    return df
