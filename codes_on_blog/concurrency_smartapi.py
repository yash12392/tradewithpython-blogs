"""
Author: Yash Roongta
Detailed Implementation: https://tradewithpython.com/concurrency-in-python-using-smartapi
You will have to give it a trade file to test this code, one sample file can be 
downloaded from here: https://app.blackhole.run/#8rolv6L2ED15oAuBM5GPcB2ghULBkAbRhdTeAF5nDNDM

You will also have to supply your own SmartAPI credentials.
"""

from smartapi import SmartConnect
import pandas as pd
from datetime import datetime
import time, concurrent.futures

obj = SmartConnect(api_key = "your_api_key")
#this obj will be used later on to make all the trade requests.

#Let's login
data = obj.generateSession("Your Client ID","Your Password")

#verifying if the login was successful
print(data)

df = pd.read_excel("path/to/file.xlsx")
#print(df.head())

trade_list = [] #empty list

#looping over each row in the dataframe and storing
#the value in each column to generate orderparams dict
#we use str to convert to strings
for index, rows in df.iterrows():
    new_dict = {"variety": str(rows['variety']), 
                "tradingsymbol" : str(rows['tradingsymbol']),
                "symboltoken" : str(rows['symboltoken']),
                "transactiontype": str(rows['transactiontype']), 
                "exchange": str(rows['exchange']),
                "ordertype": str(rows['ordertype']), 
                "producttype": str(rows['producttype']),
                "duration": str(rows['duration']), 
                "price": str(rows['price']), 
                "quantity": str(rows['quantity']),
                "triggerprice": str(rows['triggerprice'])}

    trade_list.append(new_dict)

print(trade_list)

def place_order(orderparams):
    try:
        orderID = obj.placeOrder(orderparams)
        print("The order id is: {}".format(orderID))
    except Exception as e:  #1st error
        time.sleep(1) #ensure you have imported time at the top
        try:
            orderID = obj.placeOrder(orderparams)
            print("The order id is: {}".format(orderID))
        except Exception as e: #2nd error
            time.sleep(1)
            try:
                orderID = obj.placeOrder(orderparams)
                print("The order id is: {}".format(orderID))
            except Exception as e:
                print("Order placement failed: {}".format(e))

def place_multiple_orders(tradeList):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(place_order, tradeList)

start = datetime.now()

place_multiple_orders(trade_list)

end = datetime.now()
print(end - start)

############  END ##################
