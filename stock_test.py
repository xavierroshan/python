import yfinance as yf
import pandas as pd

# Define the list of tickers
tickers = ['AAPL', 'AMZN', 'MA', 'V']

# Define the list of keys to remove
values_list = [
    'address1','city','state','zip','country', 'phone','industryKey', 'website','sectorKey','industryDisp',
    'sectorDisp', 'longBusinessSummary', 'fullTimeEmployees',
    'companyOfficers', 'auditRisk', 'boardRisk', 'compensationRisk', 'shareHolderRightsRisk',
    'overallRisk', 'governanceEpochDate', 'compensationAsOfEpochDate', 'irWebsite', 'maxAge',
    'priceHint', 'open', 'dayLow', 'dayHigh', 'regularMarketOpen', 'regularMarketDayLow',
    'regularMarketDayHigh', 'volume', 'regularMarketVolume', 'averageVolume',
    'averageVolume10days', 'averageDailyVolume10Day', 'bid', 'ask', 'bidSize', 'askSize',
    'financialCurrency', 'exchange', 'quoteType', 'symbol', 'underlyingSymbol', 'shortName',
    'longName', 'firstTradeDateEpochUtc', 'timeZoneFullName', 'timeZoneShortName', 'uuid',
    'messageBoardId', 'gmtOffSetMilliseconds', 'targetHighPrice', 'targetLowPrice',
    'targetMeanPrice', 'targetMedianPrice', 'recommendationMean', 'recommendationKey',
    'numberOfAnalystOpinions', 'lastSplitFactor', 'lastSplitDate', 'lastFiscalYearEnd',
    'nextFiscalYearEnd', 'mostRecentQuarter', 'lastDividendValue', 'lastDividendDate'
]

# Create an empty dictionary to store the data
data = {}

# Loop through the tickers and retrieve the data
for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.info
    
    # Remove the keys from the info dictionary
    for key in values_list:
        if key in info:
            del info[key]
    
    # Add the data to the dictionary
    data[ticker] = info

# Create the DataFrame
df = pd.DataFrame.from_dict(data, orient='index')
print(df)

# Write the DataFrame to a CSV file
df.to_csv('stock_data.csv', index=True)

print("Data exported to 'stock_data1.csv'")