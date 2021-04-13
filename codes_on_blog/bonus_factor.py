"""
Author: Yash Roongta
Detailed Implementation: https://tradewithpython.com/cleaning-splits-and-bonus-data-using-python
Any comments/feedback/questions, please reach out to me on Linkedin/Twitter, links in the article.

"""

import pandas as pd

bonus = pd.read_csv('path/to/bonus.csv')
bonus.columns = bonus.columns.str.strip() #stripping all whitespaces in columns.

#dropping unnecessary columns
bonus.drop(['Security Code','Company Name', 'Record Date', 'BC Start Date', 'BC End Date', 'ND Start Date',
       'ND End Date', 'Actual Payment Date'], axis=1, inplace=True)

#adding a new column ratio which will contain the a:b ratio extracted from Purpose column.
bonus['ratio'] = bonus.apply(lambda x: x['Purpose'].split(' ')[-1], axis=1)

def split_ratio_cols(series):
    '''
    Function to split the a:b ratio into a series and b series.
    series: ratio column in form of pd.Series.

    Outputs:
    num: a in a:b in the form of pd.Series
    denom: b in a:b in form of pd.Series
    '''
    num_list = []
    denom_list = []
    
    for ratio in series:
        try:
            num_list.append(ratio.split(':')[0])
        except IndexError:
            num_list.append(None)
        try:
            denom_list.append(ratio.split(':')[1])
        except IndexError:
            denom_list.append(None)
            
    return num_list, denom_list

def convert_float(x):
    try:
        return float(x)
    except ValueError:
        return None
    except TypeError:
        return None

#converting the ratio column to two new columns numerator and denominator.
num, denom = split_ratio_cols(bonus['ratio'])
bonus['numerator'] = num
bonus['denominator'] = denom

#converting both num,denom columns to float
bonus['numerator'] = bonus['numerator'].apply(convert_float)
bonus['denominator'] = bonus['denominator'].apply(convert_float)

#dropping all NA items which will have to be adjusted manually. 
bonus.dropna(axis=0,inplace=True, subset=['numerator', 'denominator'] )

#stripping all values in a dataframe of all whitespaces.
bonus = bonus.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

#Some values might not have correct bonus info and may come as 0:0, e.g. IGARASHI on 26th Sep
#Again, need to manually adjust such instances and best to drop it from dataframe
bonus = bonus[bonus.denominator != 0]

#assiging a new column bonus_factor
bonus['bonus_factor'] = bonus.apply(lambda x: (x['denominator']/(x['numerator'] + x['denominator'])), axis=1)

bonus['Ex Date'] = pd.to_datetime(bonus['Ex Date'])
bonus.sort_values('Ex Date', ascending = False, inplace = True)

print(bonus.head())