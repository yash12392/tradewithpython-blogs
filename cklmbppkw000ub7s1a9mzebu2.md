## How to Download End-of-Day Stock Prices for National Stock Exchange of India using Python?

Welcome Readers 🤩 to the first article in the series **"NSE EOD Stock Prices"**.

This article will cover the best way to download the End-Of-Day stock prices for every stock listed on the  [National Stock Exchange of India](https://www.nseindia.com/)  using Python without any sweat.

So without any delay, let's get started!! Because I am excited 🤭

#### We will be covering the following points in this article:
1. What is NSE Bhavcopy File?
2. How to download the NSE Bhavcopy File using Python?

**So let's jump in 🤹‍♂️**

### What is NSE Bhavcopy File?

**Bhavcopy's** literal translation in Hindi would be **"stock-price sheet"**, and it fits in with the name because the Bhavcopy File will have all the end-of-day details of the securities trading on the exchange. You can download a sample Bhavcopy File by clicking  [here.](https://archives.nseindia.com/products/content/sec_bhavdata_full_18022021.csv) 

Consider Bhavcopy as a high-level snapshot of all trading activity for the day, which everyone in the industry can use. The following details are available in this File:

*(Scroll below to see sample image to make sense of below points)*

- **SYMBOL: **The latest official symbol of the traded security.
- **SERIES: **The latest Series the traded security is on (E.g., "EQ" for Equity, "BE" for Compulsory Delivery),  [TickerTape](https://www.tickertape.in/)  has a good blog on this, you can read more about it  [here. ](https://blog.tickertape.in/nse-stock-series-what-do-they-mean-and-which-category-is-for-you/). Frankly, for this project, we will only be dealing with the `["EQ", "BE", "SM"]` series.
- **DATE1: **This will be the same date for which you are accessing the File.
- **PREV_CLOSE: **T-1B closing price of the security (T: Trading Day, B: Business Day)
- **OPEN_PRICE: **The opening price of the security at 09:15 AM IST. 
- **HIGH_PRICE: **The highest price of the security during the trading day.
- **LOW_PRICE: **The lowest price of the security during the trading day.
- **CLOSE_PRICE: **The closing price of the security at 15:30 IST. The closing price is the weighted average price of the last 30 mins of trading. 
- **LAST_PRICE: **The actual last traded price of the security which can differ from *CLOSE_PRICE*
- **AVG_PRICE: **The Volume Weighted Average Price of the security for the trading day.
- **TTL_TRD_QNTY: **The total units of security traded.
- **TURNOVER_LACS: **The total value of all the units of the security traded in Lakhs.
- **NO_OF_TRADES: **The total number of trades for that security for the day. (E.g., one trade might have 100 units of BUY and another might have 20 units of BUY, this will be considered as 2 total trades)
- **DELIV_QTY: **This is `TTL_TRD_QNTY - INTRADAY_TRADES`, which means how many security units have been accepted for actual delivery in Demat accounts. 
- **DELIV_PER: **This is `DELIV_QTY/TTL_TRD_QNTY`

I am sure you would now understand the importance of this File; this is the golden source of data used by most market participants whose trading strategies depend on EOD data. The preliminary data is released every day at ** 15:40 IST** but the majority of data becomes available at ** 16:00 IST**

***Below is the snapshot of the sample file which was given in the link above.***

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613951312714/21qQpMawy.png)

### How to download the NSE Bhavcopy File using Python?

Here comes the **secret sauce 🥣**, How do you download this File daily using Python, and how do you do it over the last 5 Years by running your code in a loop?

To be honest, it is really easy and tempting to create your own program using the `requests` library of Python, which can do this task for you every day after 16:00 IST to collect this data. But why reinvent the wheel when there are already several options out there?

Introducing `jugaad-data` library by `jugaad-py`

%[https://github.com/jugaad-py/jugaad-data]

This library is the easiest to use with its simple to understand syntax; it also supports the new NSE website. It can download bhavcopies for **Stocks, Futures & Options, Indexes, Index Futures, and Options** with a single line of code. It also supports **caching** which is cool. If that wasn't enough, it also supports fetching the **live prices** of particular security from NSE website, but I will **caution you** to use that, given we don't want to make too many requests to NSE who can block our IP address. The detailed documentation of this API can be found  [here.](https://marketsetup.in/documentation/jugaad-data/)  

> I wanted to let the readers know that this is not an official API by NSE, and I am in no way associated with this API. 

***Before we get into coding, if you don't have `jugaad-data` installed on your machine, just type in `pip install jugaad-data`, and that should do the job. ***

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613953045636/-SyC6O0qH.png)

#### Step 1: Testing how the output looks like

```Python
#Making all necessary imports for the code
from datetime import date
from jugaad_data.nse import full_bhavcopy_save

#Saving the Bhavcopy file for 01-01-2021
full_bhavcopy_save(date(2021,1,1), "path/to/folder")

#Tip: You can use "." instead of "path/to/folder"
#If you want to save your File where your code file is. 
#If unsure where your code file is, import os and run os.getcwd()
```
Can you believe it? That was it! Yes, for real, it's that sample to save the bhavcopy for any particular date; once you run the above, the `sec_bhavdata_full_01Jan2021bhav.csv` should be saved in the path you defined. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613953579169/46behS60u.png)

**Things to Note:**
- There are two functions in the `jugaad-data` library, one is `bhavcopy_save` and the other is `full_bhavcopy_save`, we are using the latter one as it has more information on delivery qty and percentage which can be very useful.
- If you run the function `full_bhavcopy_save` for any date where the stock market is closed, it will download the data for the last traded day, but the file name will be saved as the day you requested.
- If you run the function for a future date, it will give you an ugly-looking error like this because it cannot find data on the NSE website for that day. This will also happen if you try to get this File before 16:00 IST for the day.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613953878244/nVUB7NSm_.png)

#### Step 2: How to download the Bhavcopy File for a range of dates?

This sounds simple to do, and you must have thought to do this in a `for` loop in Python, but there are a few complexities here, we need to account for **"Weekends"** and **"Stock Exchange Holidays"** in our code. Otherwise, we might get that ugly-looking error I showed above, or we will be downloading duplicate files over the weekend for the data we already have. 

Don't worry, `pandas` has a special function, `bdate_range`, which will make our lives easier. Let's try and generate a `date_range` between `01-12-2020` to `31-12-2020`, which has a couple of holidays.

```python
import pandas as pd
from jugaad_data.holidays import holidays

date_range = pd.bdate_range(start='12/01/2020', end = '12/31/2020', 
                         freq='C', holidays = holidays(2020,12))

# start and end dates in "MM-DD-YYYY" format
# holidays() function in (year,month) format
#freq = 'C' is for custom

print(date_range)
```

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613955203197/tfyyy7WVF.png)
As you can see in the screenshot above, all **weekends** have been excluded, and **public holidays** like Christmas have also been excluded. 

Let's go ahead and now download this data for the whole of 2020 in one go; you can download going back as much as you want, but I wouldn't advise you to do that in one go as too many requests to NSE servers from your IP address may get you blocked. 

```python
date_range_2020 = pd.bdate_range(start='01/01/2020', end = '12/31/2021', 
                    freq='C', holidays = holidays(2020))

dates_2020 = [x.date() for x in date_range_2020]
#This is known as a list comprehension; let's print it out to see what happens

print(dates_2020)
```
![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613955762484/485_bDunU.png)

You can see the difference between the two dates, the first one is a Pandas `DatetimeIndex` and the second one is a `datetime.date`, we have to use the latter because that's supported by `jugaad-data`, look at the very first example where we give it `date(2021,1,1)`

```Python
from random import randint
import time

for dates in dates_2020:
     try:
          full_bhavcopy_save(dates, "path/to/folder")
          time.sleep(randint(1,4)) #adding random delay of 1-4 seconds
     except (ConnectionError, ReadTimeoutError) as e:
          time.sleep(10) #stop program for 10 seconds and try again.
          try:
               full_bhavcopy_save(dates, "path/to/folder")
               time.sleep(randint(1,4))
          except (ConnectionError, ReadTimeoutError) as e:
               print(f'{dates}: File not Found')
```

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613957775314/hEva3Azcj6.png)

>Update: As of 22/02/2021, the NSE website is throwing a 404 error for the full_bhavcopy File for 13/04/2020 and 28/09/2020, the reason is unknown, and I have emailed NSE about it. The code might crash; just restart the script after changing the start date, for example, if it crashes for 28/09/2020, just mention the start date as 29/09/2020 and re-run.

And that's it, it will take a while to download the whole year's data in one go given the random delay of 1-4 seconds, but the process should be smooth, and you will see files appearing in the path you have defined. 

You must have noticed the `try` and `except` method in the code; that's called exception handling; make sure to google more about it later. 

That's it for today, folks; I hope you enjoyed this article and our approach to download this data programmatically. In the next article, we will discuss more what to do with so many data files and how to store them in time-series format. Remember subscribing to **my newsletter 📬** to get regular updates.  

If you need any help with the above or need some more information, you can ping me on  [Twitter](https://twitter.com/yash_roongta?lang=en)  or [Linkedin.](https://www.linkedin.com/in/yashroongta/)  

If you like it up till now, consider buying me a coffee ☕ by  [clicking here](https://www.buymeacoffee.com/tradewithyash)  or the button below.

%%[buymeacoffee-btn]



