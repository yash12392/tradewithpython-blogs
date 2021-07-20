'''
Author: Utkarsh Singhal
Blog Link: https://tradewithpython.com/building-an-optimal-portfolio-with-python

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import date
from nsepy import get_history as gh
plt.style.use('fivethirtyeight')

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import  risk_models
from pypfopt import expected_returns
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

stocksymbols = ['TATAMOTORS','DABUR', 'ICICIBANK','WIPRO','BPCL','IRCTC','INFY','RELIANCE']
startdate = date(2019,10,14)
end_date = date.today()
print(end_date)
print(f"You have {len(stocksymbols)} assets in your porfolio" )

df = pd.DataFrame()
for i in range(len(stocksymbols)):
    data = gh(symbol=stocksymbols[i],start=startdate, end=(end_date))[['Symbol','Close']]
    data.rename(columns={'Close':data['Symbol'][0]},inplace=True)
    data.drop(['Symbol'], axis=1,inplace=True)
    if i == 0:
        df = data
    if i != 0:
        df = df.join(data)

# calculating expected annual return and annualized sample covariance matrix of daily assets returns

mean = expected_returns.mean_historical_return(df)

S = risk_models.sample_cov(df) # for sample covariance matrix

plt.style.use('ggplot')
fig = plt.figure()
sb.heatmap(S,xticklabels=S.columns, yticklabels=S.columns,
cmap='RdBu_r', annot=True, linewidth=0.5)
print('Covariance between daily simple returns of stocks in your portfolio')
plt.show(fig)

ef = EfficientFrontier(mean,S)
weights = ef.max_sharpe() #for maximizing the Sharpe ratio #Optimization
cleaned_weights = ef.clean_weights() #to clean the raw weights
# Get the Keys and store them in a list
labels = list(cleaned_weights.keys())
# Get the Values and store them in a list
values = list(cleaned_weights.values())
fig, ax = plt.subplots(figsize=(10, 20))
ax.pie(values, labels = labels, autopct='%1.0f%%')
print('Portfolio Allocation')
plt.show(fig)

ef.portfolio_performance(verbose=True)

portfolio_amount = float(input("Enter the amount you want to invest: "))
if portfolio_amount != '' :
    # Get discrete allocation of each share per stock

    latest_prices = get_latest_prices(df)
    weights = cleaned_weights
    discrete_allocation = DiscreteAllocation(weights, latest_prices , total_portfolio_value = int(portfolio_amount))
    allocation , leftover = discrete_allocation.lp_portfolio()

    discrete_allocation_list = []


    for symbol in allocation:
        discrete_allocation_list.append(allocation.get(symbol))


    portfolio_df = pd.DataFrame(columns =['Ticker' , 'Number of stocks to buy'])

    portfolio_df['Ticker'] = allocation
    portfolio_df['Number of stocks to buy'] = discrete_allocation_list
    print('Number of stocks to buy with the amount of ₨ ' + str(portfolio_amount))
    print(portfolio_df)
    print('Funds remaining with you will be: ₨' , int(leftover))

