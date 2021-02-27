"""
Author: Yash Roongta
Detailed Implementation: https://tradewithpython.com/how-to-capture-all-nse-bhavcopy-eod-stock-prices-files-into-one-file
You will have to give the code a filepath where all bhavcopy .csv have been downloaded and
a destination path for the final csv file.
"""


file_list = glob.glob('path/to/folder/where/files/saved/*.csv')
#Notice the * which acts as a wildcard.
#This will give you the path of all files with .csv extension in that folder


final_df = pd.DataFrame() #empty dataframe

for csv_file in file_list:
    df = pd.read_csv(csv_file)
    csv_file_name = csv_file.split('\\')[7]
    print('Processing File : {}'.format(csv_file_name))
    df.columns = df.columns.str.replace(' ', '')
    df['DATE1'] = pd.to_datetime(df['DATE1'])
    df.set_index(['DATE1'], inplace=True)
    df.drop(['LAST_PRICE', 'PREV_CLOSE'], axis=1, inplace=True)

    df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    new_df = df[df['SERIES'].isin(['EQ', 'BE', 'SM'])]
    final_df = final_df.append(new_df)

final_df.sort_index(inplace=True) #to sort by dates


final_df.to_csv('path/to/folder/bhavcopy_2020_data.csv')
