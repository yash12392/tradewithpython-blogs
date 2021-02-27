```
Author: Yash Roongta
The code in this file is for the blog written here: https://tradewithpython.com/equity-index-score-esg-with-python

Please read the blog for detailed usage instructions, a couple of high level points.
1. You will have to provide the Yahoo Finance Tickers to the code.
2. Fetching ESG data and Stock Data will take time due to random delay function embedded.
3. The output will be printed in your console.
    
```

import pandas as pd
import yfinance as yf
import time
from random import randint

df = pd.read_csv('/path/to/file.csv') #give the full path of file downloaded
index_tickers = df['Symbol'].tolist() #assigning all tickers to a list
#print(index_tickers)

esg_data = pd.DataFrame() #empty df for attaching all ticker's data response

for ticker in index_tickers:
     print(ticker) #just FYI to know your code is running
     ticker_name = yf.Ticker(ticker)
     try:
          if ticker_name.sustainability is not None: #if no response from Yahoo received, it will pass to next ticker
               ticker_df = ticker_name.sustainability.T #response dataframe
               ticker_df['symbol'] = ticker #adding new column 'symbol' in response df
               esg_data = esg_data.append(ticker_df) #attaching the response df to esg_data
               time.sleep(randint(2,8)) #delaying the fetch of data for 2-8 seconds
     except (IndexError, ValueError) as e: #in case yfinance API misbehaves
          print(f'{ticker} did not run') #FYI
          pass
				
esg_tickers = esg_data['symbol']
no_esg_data = list(set(index_tickers) - set(esg_tickers))
#set function removes all duplicates in a list and the above gives us the
#difference between our original ticker list and our esg_data ticker list
#print(no_esg_data)

new_esg_df = esg_data[['symbol', 'socialScore', 
               'governanceScore', 'totalEsg', 'environmentScore']]
#the above basically takes the columns mentioned above and assigns into new df.
#new_esg_df.head(5) #let's see what it looks like

main_df = pd.DataFrame() #creating empty df to store data

for ticker in index_tickers:
     ticker_name = yf.Ticker(ticker)
     try:
          ticker_info = ticker_name.info
          ticker_df = pd.DataFrame.from_dict(ticker_info.items()).T
          #the above line will parse the dict response into a DataFrame
          ticker_df.columns = ticker_df.iloc[0]
          #above line will rename all columns to first row of dataframe
          #as all the headers come up in the 1st row, next line will drop the 1st line
          ticker_df = ticker_df.drop(ticker_df.index[0])
          main_df = main_df.append(ticker_df)
          time.sleep(randint(2,8))
          print(f'{ticker} + Complete')
     except (IndexError, ValueError) as e:
          print(f'{ticker} + Data Not Found')

filtered_df = main_df[['symbol', 'sector', 'previousClose', 'sharesOutstanding']]
#filtered_df.head(5) #checking how first 5 rows look like

filtered_df['newMarketCap'] = filtered_df['previousClose'] * filtered_df['sharesOutstanding']
total_index_mcap = filtered_df['newMarketCap'].sum()
filtered_df['marketWeight'] = ((filtered_df['newMarketCap']/total_index_mcap)*100)

final_df = filtered_df.merge(new_esg_df, how='left', on='symbol')
#for more info on .merge visit https://bit.ly/3pFlYIm


final_esg_df = pd.DataFrame() #empty df

sector_list = final_df['sector'].unique().tolist() #getting list of sectors in index

#looping over each sector and apply .mean to calculate average
for sector in sector_list:
    sector_df = final_df[final_df['sector'] == sector]
    sector_df['socialScore'].fillna(round(sector_df['socialScore'].mean(),2), inplace=True)
    sector_df['governanceScore'].fillna(round(sector_df['governanceScore'].mean(),2), inplace=True)
    sector_df['totalEsg'].fillna(round(sector_df['totalEsg'].mean(),2), inplace=True)
    sector_df['environmentScore'].fillna(round(sector_df['environmentScore'].mean(),2), inplace=True)

    final_esg_df = final_esg_df.append(sector_df)

#also adding the weighted average columns into this new final_esg_df
final_esg_df['mktweightedEsg'] = (final_esg_df['marketWeight'] * final_esg_df['totalEsg'])/100
final_esg_df['mktweightedEnvScore'] = (final_esg_df['marketWeight'] * final_esg_df['environmentScore'])/100
final_esg_df['mktweightedSocScore'] = (final_esg_df['marketWeight'] * final_esg_df['socialScore'])/100
final_esg_df['mktweightedGovScore'] = (final_esg_df['marketWeight'] * final_esg_df['governanceScore'])/100

print(f'Total Environment Score: {round(final_esg_df['mktweightedEnvScore'].sum(),2)}')
print(f'Total Social Score: {round(final_esg_df['mktweightedSocScore'].sum(),2)}')
print(f'Total Governance Score: {round(final_esg_df['mktweightedGovScore'].sum(),2)}')
print(f'Total ESG Score: {round(final_esg_df['mktweightedEsg'].sum(),2)}')

