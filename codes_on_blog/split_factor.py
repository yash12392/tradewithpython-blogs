"""
Author: Yash Roongta
Detailed Implementation: https://tradewithpython.com/cleaning-splits-and-bonus-data-using-python
Any comments/feedback/questions, please reach out to me on Linkedin/Twitter, links in the article.

"""

import pandas as pd
import re #to conduct regex operations.

split = pd.read_csv('path/to/Split.csv')

split.columns = split.columns.str.strip() #stripping all whitespaces in column names

split.drop(['Security Code', 'Company Name', 'Record Date', 'BC Start Date', 'BC End Date', 
            'ND Start Date','ND End Date', 'Actual Payment Date'], axis=1, inplace=True)

def split_columns(series):
    '''
    Function to take in the purpose column and apply regex operations 
    to parse two numbers in the string.
    series: purpose column in form of pd.Series.

    Outputs:
    num: pd.Series
    denom: pd.Series
    '''
    num = []
    denom = []
    
    for ratio in series:
        ratio_list = re.findall(r'[0-9]+', ratio)
        
        if len(ratio_list) == 2:
            num.append(ratio_list[0])
            denom.append(ratio_list[1])
        else:
            num.append(None)
            denom.append(None)
    
    return num, denom

def convert_float(x):
    try:
        return float(x)
    except ValueError:
        return None
    except TypeError:
        return None

#applying function to generate two new series
#assigning these series to two new columns in split df.
num, denom = split_columns(split['Purpose'])
split['numerator'] = num
split['denominator'] = denom

#converting num, denom column to floats
split['numerator'] = split['numerator'].apply(convert_float)
split['denominator'] = split['denominator'].apply(convert_float)

#dropping all NA items which will have to be adjusted manually. 
split.dropna(axis=0,inplace=True, subset=['numerator', 'denominator'] )

#Stripping whitespaces in the entire dataframe.
split = split.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

#assiging a new column split_factor
split['split_factor'] = split.apply(lambda x: x['denominator']/x['numerator'], axis=1)

split['Ex Date'] = pd.to_datetime(split['Ex Date'])
split.sort_values('Ex Date', ascending = False, inplace = True)

print(split.head())