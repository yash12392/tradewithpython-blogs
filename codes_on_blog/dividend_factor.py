"""
Author: Yash Roongta
Detailed Implementation: https://tradewithpython.com/cleaning-stock-dividend-data-using-python-pandas-and-calculating-dividend-factor
Any comments/feedback/questions, please reach out to me on Linkedin/Twitter, links in the article.

"""

import pandas as pd

############################# PART 1 ##################################################

divd = pd.read_csv('path/to/dividends.csv')

divd.columns = divd.columns.str.strip() #stripping all whitespaces

#dropping unnecessary columns
divd.drop(labels = ['Record Date', 'BC Start Date', 'BC End Date', 'ND Start Date',
       'ND End Date', 'Actual Payment Date', 'Company Name', 'Security Code'], inplace = True, axis=1)

#adding new column div_value which contains the numeric dividend value in str dtype
divd['div_value'] = divd.apply(lambda x: x['Purpose'].split('-')[-1].strip(), axis=1)

#https://stackoverflow.com/questions/23602061/exception-handling-when-changing-pandas-dataframe-type
def convert_float(x):
    try:
        return float(x)
    except ValueError:
        return None
    except TypeError:
        return None

#converting div_value column values to float and assigning Null values to non-numeric values.
divd['div_value'] = divd['div_value'].apply(convert_float)

#dropping all null values.
divd.dropna(axis=0,inplace=True, subset=['div_value'] )

#Removing all whitespaces
divd = divd.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

#converting ex-date to datetime and sorting it in Descending
divd['Ex Date'] = pd.to_datetime(divd['Ex Date'])
divd.sort_values('Ex Date', ascending = False, inplace=True)

############################# PART 2 ##################################################

price_df = pd.read_csv('path/to/file/nse_prices_final_2020.csv')

#Finding stocks common in divd dataframe and price_df
actual_divd_stocks = list(set(price_df['SYMBOL'].unique()) & set(divd['Security Name'].unique()))

#Filtering divd dataframe for common securities and dates we are working with in the article.
divd = divd[divd['Security Name'].isin(actual_divd_stocks)]
divd = divd[(divd['Ex Date'] < '2020-12-31') & (divd['Ex Date'] > '2016-01-01')]

def get_last_px(df, name, date, div_amt):
    
    '''
    Function to get the last closing price of the security before Ex-Date.
    df = Takes in Price Dataframe
    name = Name of the Stock which gave Dividend
    date = Ex-Date
    div_amt = The Dividend Amount

    Outputs:
    last_px = Last Close Price before Ex-Date
    If Stock not found in price_df, last_px is div_amt.
    '''
    try:
        last_px = df[df['SYMBOL'] == name].loc[:date].iloc[-2]['CLOSE']
    except IndexError:
        last_px = div_amt
    
    return last_px


divd['dividend_factor'] = divd.apply(lambda x: (1 - (x['div_value']/get_last_px(price_df, x['Security Name'], 
                                                            x['Ex Date'], x['div_value']))) , axis=1)

print(divd.head())

############################# THE END ##################################################