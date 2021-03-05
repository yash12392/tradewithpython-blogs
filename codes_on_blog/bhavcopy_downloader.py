"""
Author: Yash Roongta
On running this code, you can download full_bhavcopy from new NSE website into the path you define.
The user is also expected to give the correct dates and holidays, read comments in code to know more.
"""


#Making all necessary imports for the code
from datetime import date
from jugaad_data.nse import bhavcopy_save
import pandas as pd
from jugaad_data.holidays import holidays
from random import randint
import time, os

date_range = pd.bdate_range(start='12/01/2020', end = '12/31/2020', 
                         freq='C', holidays = holidays(2020,12))
                         
savepath = os.path.join('C:', os.sep, 'Give_Your_Own_path')
                                                  
# start and end dates in "MM-DD-YYYY" format
# holidays() function in (year,month) format
#freq = 'C' is for custom

dates_list = [x.date() for x in date_range]

for dates in dates_list:
     try:
          bhavcopy_save(dates, savepath)
          time.sleep(randint(1,4)) #adding random delay of 1-4 seconds
     except (ConnectionError, ReadTimeoutError) as e:
          time.sleep(10) #stop program for 10 seconds and try again.
          try:
               bhavcopy_save(dates, savepath)
               time.sleep(randint(1,4))
          except (ConnectionError, ReadTimeoutError) as e:
               print(f'{dates}: File not Found')
               
