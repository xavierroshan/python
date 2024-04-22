import pandas as pd
df=pd.read_csv('car_prices.csv')
#print(df)
#print(df.head(5))
#print(df.tail(5))
#print(df['year'])
#print(df['year'])
#print(df['make'])
#print(df.iloc[0:3])
#print(df.iloc[0,0])
#print(df.iloc[0:3, 1])
#print(df.iloc[0:3,0:3])
#print(df.describe)
#print(df.info)
#print(df.iloc[:,:])
#df = df.iloc[::-1]
#print(df)
#df = df.iloc[:, ::-1]
#print(df)
#sort_df = df.sort_values(by='sellingprice', ascending=True)
#print(sort_df.iloc[10000:10100])
#filtered_df = df[df['year']<2000]
#print(filtered_df)

for index, row in df.iterrows():
    if index==1:
        print(row)
