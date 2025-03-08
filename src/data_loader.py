import pandas≈ as pd

def load_data(file_path="data/Test.xlsx"):
    """Loads and cleans portfolio data from Excel file."""
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip()  # Remove spaces from column names
    df['Date'] = pd.to_datetime(df['Date'])  # Convert Date to datetime format
    return df
