from sklearn.ensemble import IsolationForest

def ai_detect_anomalies(df):
    """Uses Isolation Forest to detect hidden anomalies in portfolio."""
    iso_forest = IsolationForest(contamination=0.05, random_state=42)
    df['Anomaly_Score'] = iso_forest.fit_predict(df[['Price', 'Quantity_Change', 'Closing Weights']].fillna(0))
    df['AI_Detected_Anomaly'] = df['Anomaly_Score'] == -1
    return df
