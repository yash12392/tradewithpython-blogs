"""
Author: Yash Roongta
Detailed Implementation: https://tradewithpython.com/adjust-time-series-data-for-ticker-changes
You will have to give the code a filepath where the symbol_change_dd.mm.yyyy.csv file will be downloaded.

You will also need a NSE Stock Prices dataset to work with for using this code, you can access this data
in data_on_blog folder in this repo. The data is however in parquet format as .csv was too large to upload on Github.

You can use pd.read_parquet() instead of pd.read_csv() to get that data into a dataframe. Enjoy!
"""

#Making all necessary imports
import pandas as pd
import os, requests
from datetime import datetime, date

#URL from where file can be downloaded.
nse_symbol_path = 'https://www1.nseindia.com/content/equities/symbolchange.csv'

r = requests.get(nse_symbol_path) #getting the file.

print(r.status_code) #to check if the request was successful.

filename = f'symbol_change_{datetime.now().strftime("%d.%m.%Y")}.csv'
#The datetime function will give you the current date.

open(f'path/to/folder/{filename}', 'wb').write(r.content)
#This will save the file in the folder you defined.

symbol_df = pd.read_csv('path/to/folder/symbol_change_dd.mm.yyyy.csv')

#deleting all whitespace from column names and dataset.
symbol_df.columns = symbol_df.columns.str.replace(' ', '')
symbol_df = symbol_df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

#converting the date column to datetime dtype.
symbol_df['SM_APPLICABLE_FROM'] = pd.to_datetime(symbol_df['SM_APPLICABLE_FROM'])

#very important, sorting values by date
symbol_df.sort_values(by ='SM_APPLICABLE_FROM', axis=0, inplace=True)

#Filtering for point 2 above.
new_sym_df = symbol_df[(symbol_df['SM_APPLICABLE_FROM'] <= pd.to_datetime('today').floor('D'))]

#Creating a dictionary of symbol changes.
symbol_change_dict = dict(zip(new_sym_df.SM_KEY_SYMBOL, new_sym_df.SM_NEW_SYMBOL))

#print(symbol_change_dict)


stock_price_df = pd.read_csv('path/to/your/existing/data.csv', 
                         index_col = 'DATE1')

for keys in symbol_change_dict.keys():
     print(f'Processing {keys} symbol')
     stock_price_df.replace(to_replace = keys, 
                         value = symbol_change_dict[keys], inplace = True)

#saving this new dataset with updated symbols
stock_price_df.to_csv('path/to/folder/new_data.csv')

