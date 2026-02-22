import pandas as pd

def create_features(df):

    df = df.copy()

    # Lag features
    df['Price_lag1'] = df['Price'].shift(1)
    df['Price_lag2'] = df['Price'].shift(2)

    # Rolling averages
    df['Price_roll3'] = df['Price'].rolling(3).mean()
    df['Price_roll5'] = df['Price'].rolling(5).mean()

    # Seasonality
    df['Month'] = df['Date'].dt.month
    df['Week'] = df['Date'].dt.isocalendar().week

    df = df.dropna()

    return df