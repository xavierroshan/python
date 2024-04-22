import pandas as pd
df=pd.read_csv('car_prices.csv')
#filtered_df = df[(df['make']=='Dodge') & (df['model']=='Avenger')]
#print(filtered_df)
#sorted_df = df.sort_values(by =['year','transmission', 'odometer'], ascending=[1,1,0])
#print(sorted_df)
#df = df.iloc[0:4, 0:4]
#print(df)
#df = df.loc['year']
#print(df)
df['Ratio']=df['sellingprice']/df['odometer']
print(df)
df=df.drop(columns='Ratio')
print(df)

