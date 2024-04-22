import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Specify the file path
file_path = '/Users/xavierroshan/Desktop/Learning/Python/studysession/user_data.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Extract the stock symbols from the first column, excluding null values
stock_symbols = df.iloc[:, 0].dropna().tolist()

# Create an empty dictionary to store the historical data
historical_data = {}

# Retrieve the historical data for each stock symbol
for symbol in stock_symbols:
    try:
        stock = yf.Ticker(symbol)
        historical_df = stock.history(period="max")
        historical_data[symbol] = historical_df
    except Exception as e:
        print(f"Error retrieving data for {symbol}: {e}")

# Prompt the user to select a stock
while True:
    print("Available stocks:")
    for symbol in stock_symbols:
        print(symbol)
    
    selected_stock = input("Enter the stock symbol you want to view (or 'q' to quit): ").upper()
    
    if selected_stock == 'Q':
        break
    
    if selected_stock in historical_data:
        print(f"Historical data for {selected_stock}:")
        historical_df = historical_data[selected_stock]
        print(historical_df)
        
        # Plot the trend chart
        plt.figure(figsize=(12, 6))
        historical_df['Close'].plot()
        plt.title(f"{selected_stock} Stock Price Trend")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.grid()
        plt.show()
    else:
        print(f"Sorry, {selected_stock} is not a valid stock symbol.")