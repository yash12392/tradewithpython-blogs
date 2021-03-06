## How to Capture all NSE Bhavcopy (EOD Stock Prices) Files into One File?

Welcome Readers 🤩 to the second article in the series **"NSE EOD Stock Prices"**
This article will be taking the inputs of the **NSE Bhavcopy** files we downloaded for 2020, and we will grab the data from all these files and convert it into one single file where the index is in **time-series format.**
 
If you haven't already read the previous article, I would recommend you to do so; otherwise, this article would not make sense. 

So, let's get on with it. What does **time-series format** mean?  

Let's look at the sample below; usually, when you create an excel spreadsheet for any data, you have a column like **"Sr. No"** which starts from `1 to n`, similar to that in a time-series format that column is **"Date"**.

| Date| Symbol | Open  | High | Low | Close |
| :---:        |    :----:   |          :---: |           :---: |    :---: |    :---: |
| **2020-01-01**| KOTARISUG| 9.90 | 11.20 | 9.90 | 10.70 |
| **2020-01-02**| KOTARISUG| 10.90 | 11.00 | 10.35 | 10.70 |
| **2020-01-03**| KOTARISUG| 10.70 | 10.85| 10.40 | 10.50 |
| **2020-01-06**| KOTARISUG| 10.45 | 10.45| 9.60 | 10.00 |

So, right now, with the files we have downloaded in the last article, **"KOTARISUG"** will have a line of data in each file as long as the stock is traded/listed on the National Stock Exchange of India. 

How do we get to one file for each stock in time-series format and then save that file? It is simple, but there are a couple of nuances to deal with, let's look by loading just one sample file first; I will load `cm01Apr2020bhav.csv` for demonstration purposes. Once you know the nuances, we will do this for all the files in a loop and produce a final data file.

### Data Cleaning using Python

We will be using the existing `pandas`, `os`, `shutil`, `glob` Python libraries which come with the `Anaconda` environment for this step. 

```python
import pandas as pd
import os, shutil, glob
```
**Let's load the file into Python**

```python
df = pd.read_csv('path/to/cm01Apr2020bhav.csv')

df.head() #loading first 5 rows of the data
```

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1615006680109/PTttx1g45.png)

**Let's see some more information about this dataset we have.
**

```python
df.info()
```
![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1615006708632/AFBmAI_vK.png)

The `.info()` function gives you really important information about the data-frame like the** data-type** of each column and **total no. of entries** and how much **memory is it consuming** in your RAM. You can read a nice article about different data-types  [here.](https://pbpython.com/pandas_dtypes.html)  

You will notice we have an additional column `Unnamed: 13` which is just an empty column, so let's delete this column. 


```python
if 'Unnamed: 13' in df.columns:
     df.drop(['Unnamed: 13'], axis=1, inplace=True)

#if condition because in old files, you won't find this empty column
```

**Let's look at all the final columns in our dataframe.**

```python
df.columns #getting all columns in a list-like format.
```

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1615007080743/-1nHHkWud.png)


**Whitespaces **i.e., all leading and trailing spaces are very common, and you will come across them from time to time; the best is to get rid of them at the start, so you don't see any issues later on. The below image shows the unique entries in the `SERIES` column from another full_bhavcopy_file which has leading whitespace; However, the file we are dealing with does not have this, let's still get rid of any whitespace in the columns and the data in those columns just in case they appear in the future and break our code. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1614447305932/vm5yGl20i.png)

**Removing all Whitespaces in the DataFrame**

```python
df.columns = df.columns.str.replace(' ', '')

#we can only remove whitespace from 'object' datatype
# Hence the if condition in the below otherwise you will get an error
df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

```

**Now, let's finally clean our dataframe for the below points:**

- Convert the `TIMESTAMP` column to `datetime64` dtype; right now it is in `object` format which is not correct.
- Let's also filter our dataframe for `SERIES` categories `['EQ', 'BE', 'SM']` as all other categories are not really important to you from a retail investor point view.
- Finally, let's also set the `TIMESTAMP` column as our index, which becomes time-series data. 

```python

#Converting date column to datetime dtype
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])

#Setting DATE1 column as index
df.set_index(['TIMESTAMP'], inplace=True)

#Filtering only for EQ, BE & SM series.
new_df = df[df['SERIES'].isin(['EQ', 'BE', 'SM'])]

#Grabbing the first 5 rows of the new_df
new_df.head()
```

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1615007406032/GTYjLOKPz.png)

Also, running the `new_df.info()` to get additional details about the dataframe.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1615007424233/gT0URZ0pH.png)

**You will notice the following things:**

- The no. of entries has gone down because we filtered for particular series.
- The `Unnamed:13` column we deleted is not present.
- The memory usage is less because we now store fewer pieces of data. 

**Great stuff 🤟, now let's build a loop to do this for all the files we downloaded. **

### Building a Loop

Finally, time to build the final loop which will do the data cleaning exercise we did above for each and every file, and then attach that **clean dataframe to an existing empty dataframe.
**

But, as you will notice, the `pd.read_csv()` function expects you to give the file destination; let's quickly see how we can create a `list` of filepaths of the `.csv` files we have using the `glob` library.

```python

file_list = glob.glob('path/to/folder/where/files/saved/*.csv')
#Notice the * which acts as a wildcard.
#This will give you the path of all files with .csv extension in that folder
```
**Ensure,** you do not have any other **.csv** files in that folder as it will pick up all of them and pass them to the loop, which can crash if it gets an incorrect file.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1615007578036/gWp1u4jcb.png)

**Final Loop Code**

```python

final_df = pd.DataFrame() #empty dataframe

for csv_file in file_list:
    df = pd.read_csv(csv_file)
    csv_file_name = csv_file.split('\\')[7]
    print('Processing File : {}'.format(csv_file_name))
    df.columns = df.columns.str.replace(' ', '')
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
    df.set_index(['TIMESTAMP'], inplace=True)
    
    if 'Unnamed:13' in df.columns:
        df.drop(['Unnamed:13'], axis=1, inplace=True)
   
    df_trim = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    new_df = df_trim[df_trim['SERIES'].isin(['EQ', 'BE', 'SM'])]
    final_df = final_df.append(new_df)

final_df.sort_index(inplace=True) #to sort by dates
```
     
This shouldn't take very long to run, but once it's complete, let's call the `final_df.info()` to see our final dataframe and call the `final_df.tail()` to see the last 5 rows.

`final_df.info()`

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1615008113642/8NCwCEBAq.png)

`final_df.tail()`

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1615008125390/m1wCpsWme.png)

Finally, let's save these 428,000+ rows of the database to a **.csv** file for now. *(we will discuss what's a more efficient way of saving this in the future articles)*

```python
final_df.to_csv('path/to/folder/bhavcopy_2020_data.csv')

```
You will get a **38MB .csv file** in the path you defined, which should look like the below. Now, if you filter for **KOTARISUG** in the excel spreadsheet, you will see the time-series we showed you at the start. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1615008209196/dTr12MTA9.png)

You can also access Github  [link here](https://github.com/yash12392/tradewithpython-blogs/blob/main/codes_on_blog/bhavcopy_data_agg.py) to view the whole code in one single file directly.

That's it for today, folks; I hope you got a good insight on how to clean the data and why it's important. In the next article, we will discuss how to factor in stock_symbol changes into your dataframe and where to get that data from. **Also, do not worry about how to do this every day; we will refactor all code in the 6th article on Object-Oriented Programming, which will make it all clear.** Remember to subscribe to my newsletter 📬 to get regular updates.

If you need any help with the above or need some more information, you can ping me on  [Twitter](https://twitter.com/yash_roongta)  or  [Linkedin.](https://uk.linkedin.com/in/yashroongta) 

If you like it up till now, consider buying me a coffee ☕ by  [clicking here](https://www.buymeacoffee.com/tradewithyash)  or the button below.

%%[buymeacoffee-btn]