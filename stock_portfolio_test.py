import yfinance as yf
import pandas as pd
import os

# Constants
USER_DATA_FILE = 'user_data.csv'

# Function to save user input to a file
def save_user_input(user_data):
    # Check if the user data file exists, if not, create it
    if not os.path.exists(USER_DATA_FILE):
        if user_data:
            user_data_df = pd.DataFrame(columns=user_data[0].keys())
        else:
            user_data_df = pd.DataFrame(columns=['symbol', 'num_shares', 'cost_price'])
        user_data_df.to_csv(USER_DATA_FILE, index=False)
    
    # Process each user data entry
    for data in user_data:
        # Check if the symbol already exists in the user data file
        user_data_df = pd.read_csv(USER_DATA_FILE)
        existing_entry = user_data_df[user_data_df['symbol'] == data['symbol']]
        
        if not existing_entry.empty:
            # Update the existing entry
            existing_index = existing_entry.index[0]
            total_shares = existing_entry['num_shares'].values[0] + data['num_shares']
            new_cost_price = (existing_entry['cost_price'].values[0] * existing_entry['num_shares'].values[0] + data['cost_price'] * data['num_shares']) / total_shares
            user_data_df.at[existing_index, 'num_shares'] = total_shares
            user_data_df.at[existing_index, 'cost_price'] = new_cost_price
        else:
            # Append the new entry
            user_data_df = pd.concat([user_data_df, pd.DataFrame([data])], ignore_index=True)
        
        user_data_df.to_csv(USER_DATA_FILE, index=False)

# Get user input and save it to the file
user_input = input("Do you want to enter new stock data? (y/n) ").lower()
if user_input == 'y':
    user_input = input("Enter the stock data (format: 'symbol:AMZN,num_shares:12,cost_price:100,symbol:V,num_shares:10,cost_price:50,symbol:MA,num_shares:5,cost_price:450'): ").strip()
    user_data = []
    for entry in user_input.split(','):
        data = {}
        fields = entry.split(':')
        if len(fields) == 3:
            data['symbol'] = fields[1]
            data['num_shares'] = float(fields[2].split(',')[0])
            data['cost_price'] = float(fields[2].split(',')[1])
            user_data.append(data)
    
    # Save the user input to the file
    save_user_input(user_data)
else:
    # Create the DataFrame from the user data file
    user_data_df = pd.read_csv(USER_DATA_FILE)
    
    # Retrieve the stock data and create the DataFrame
    data = {}
    for _, row in user_data_df.iterrows():
        symbol = row['symbol']
        num_shares = row['num_shares']
        cost_price = row['cost_price']
        
        stock = yf.Ticker(symbol)
        info = stock.info
        
        # Remove the unwanted keys from the info dictionary
        values_list = [
            'address1', 'city', 'state', 'zip', 'country', 'phone', 'fax', 'industryKey', 'website', 'sectorKey', 'industryDisp',
            'sectorDisp', 'longBusinessSummary', 'fullTimeEmployees',
            'companyOfficers', 'auditRisk', 'boardRisk', 'compensationRisk', 'shareHolderRightsRisk',
            'overallRisk', 'governanceEpochDate', 'compensationAsOfEpochDate', 'irWebsite', 'maxAge',
            'priceHint', 'open', 'dayLow', 'dayHigh', 'regularMarketOpen', 'regularMarketDayLow',
            'regularMarketDayHigh', 'volume', 'regularMarketVolume', 'averageVolume',
            'averageVolume10days', 'averageDailyVolume10Day', 'bid', 'ask', 'bidSize', 'askSize',
            'financialCurrency', 'exchange', 'quoteType', 'underlyingSymbol', 'shortName',
            'longName', 'firstTradeDateEpochUtc', 'timeZoneFullName', 'timeZoneShortName', 'uuid',
            'messageBoardId', 'gmtOffSetMilliseconds', 'targetHighPrice', 'targetLowPrice',
            'targetMeanPrice', 'targetMedianPrice', 'recommendationMean', 'recommendationKey',
            'numberOfAnalystOpinions', 'lastSplitFactor', 'lastSplitDate', 'lastFiscalYearEnd',
            'nextFiscalYearEnd', 'mostRecentQuarter', 'lastDividendValue', 'lastDividendDate'
        ]

        for key in values_list:
            if key in info:
                del info[key]

        # Add the stock data, number of shares, and cost price to the data dictionary
        info['Shares'] = int(num_shares)
        info['Cost Price'] = round(cost_price, 2)
        info['Total Cost Price'] = round(num_shares * cost_price, 2)
        info['Total Current Value'] = round(num_shares * info.get('previousClose', 0), 2)
        
        #Roinding off columns
        for col in ['beta', 'trailingPE', 'forwardPE', 'marketCap', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'priceToSalesTrailing12Months',
                   'fiftyDayAverage', 'twoHundredDayAverage', 'profitMargins', 'sharesPercentSharesOut', 'heldPercentInsiders',
                   'heldPercentInstitutions', 'shortRatio', 'shortPercentOfFloat', 'bookValue', 'priceToBook', 'earningsQuarterlyGrowth',
                   'trailingEps', 'forwardEps', 'pegRatio', 'enterpriseToRevenue', 'enterpriseToEbitda', '52WeekChange', 'SandP52WeekChange',
                   'currentPrice', 'totalCashPerShare', 'quickRatio', 'currentRatio', 'debtToEquity', 'revenuePerShare', 'returnOnAssets',
                   'returnOnEquity', 'earningsGrowth', 'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 'trailingPegRatio',
                   'previousClose', 'regularMarketPreviousClose', 'Cost Price']:
            try:
                info[col] = round(info.get(col, 0), 2)
            except (TypeError, ValueError):
                info[col] = 0
        
        #Formating Columns
        try:
            info['marketCap'] = "{:,.2f}".format(info.get('marketCap', 0))
            info['enterpriseValue'] = "{:,.2f}".format(info.get('enterpriseValue', 0))
            info['floatShares'] = "{:,.2f}".format(info.get('floatShares', 0))
            info['sharesOutstanding'] = "{:,.2f}".format(info.get('sharesOutstanding', 0))
            info['sharesShort'] = "{:,.2f}".format(info.get('sharesShort', 0))
            info['sharesShortPriorMonth'] = "{:,.2f}".format(info.get('sharesShortPriorMonth', 0))
            info['sharesShortPreviousMonthDate'] = "{:,.2f}".format(info.get('sharesShortPreviousMonthDate', 0))
            info['dateShortInterest'] = "{:,.2f}".format(info.get('dateShortInterest', 0))
            info['impliedSharesOutstanding'] = "{:,.2f}".format(info.get('impliedSharesOutstanding', 0))
            info['netIncomeToCommon'] = "{:,.2f}".format(info.get('netIncomeToCommon', 0))
            info['totalCash'] = "{:,.2f}".format(info.get('totalCash', 0))
            info['ebitda'] = "{:,.2f}".format(info.get('ebitda', 0))
            info['totalDebt'] = "{:,.2f}".format(info.get('totalDebt', 0))
            info['totalRevenue'] = "{:,.2f}".format(info.get('totalRevenue', 0))
            info['freeCashflow'] = "{:,.2f}".format(info.get('freeCashflow', 0))
            info['operatingCashflow'] = "{:,.2f}".format(info.get('operatingCashflow', 0))
            info['Total Cost Price'] = "{:,.2f}".format(info['Total Cost Price'])
            info['Total Current Value'] = "{:,.2f}".format(info['Total Current Value'])
        except (TypeError, ValueError):
            pass
        
        data[symbol] = info
    
    # Create the DataFrame
    df = pd.DataFrame.from_dict(data, orient='index')

    # Move the specified columns to the end
    cols = df.columns.tolist()
    cols = [col for col in cols if col not in ['previousClose', 'regularMarketPreviousClose', 'Cost Price', 'Shares', 'Total Cost Price', 'Total Current Value']]
    cols.extend(['previousClose', 'regularMarketPreviousClose', 'Cost Price', 'Shares', 'Total Cost Price', 'Total Current Value'])
    df = df[cols]

    print(df)

# Write the DataFrame to a CSV file
df.to_csv('stock_portfolio.csv', index=True)

print("Data exported to 'stock_portfolio.csv' and 'user_data.csv'")