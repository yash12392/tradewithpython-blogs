## What are the Steps Involved in Coding your Trading Strategy?

Recently, one of my relatives, a full-time trader, contacted me to see if I can help him build a robot for his strategy; I really liked the strategy. I tracked the stock markets a couple of weeks to see if it actually pays off, and it performed decently. (>50% Win Probability)

While it is completely possible to code this strategy, I quickly realized that my full-time trader relative thought it was a simple thing to do, and that was not because of lack of appreciation of the work involved, but due to lack of knowledge of what actually goes into coding a strategy.

So I decided to write on the steps involved to code that trading strategy you might have in mind to educate everyone. 📈

### Steps to Create Your Own Robot 🤖

#### Step 1: Basic Strategy Research.

- **Idea Generation:** Identifying market patterns manually and ideating which technical indicators are required for your strategy and how are they should be used to enter and exit a position. 
- **Defining Expectations:** Having a clear understanding of what you are looking out of this strategy (like X% return on capital in X time) and how it performs in different types of market cycles.
- **Data Availability: ** Your strategy will most likely require live streaming data to see if conditions are meeting. , E.g., If your strategy depends on live market news, you need to see if you can source this data. 
- **Regulatory Hurdles: ** You will have to check if the market regulator in your country allows you to do algorithmic trading and seek approval if necessary (This is especially a requirement in India, thanks to  [Anshul Kwatra](https://www.linkedin.com/in/anshulkwatra96/) who gave a suggestion to add this point)

#### Step 2: Backtesting Your Strategy.

Assuming you have now coded your strategy in any programming language of your choice, you should test it on backdated market data to set some rough expectations for the future.

- **Period Selection: ** You will need to put some thoughts behind how backdated do you want to go and test your strategy, maybe last 6 months or last 5 years, depending on what the strategy requires.
- **Structural Changes: ** If your strategy is dependent on any economic indicators and your backtesting time period has had some structural changes to the economy (like coronavirus), you need to put some thought into if you can use this time period to set future expectations.
- **Slippages: **Quite a few times, trades do not get executed at the exact price of the ticker due to less volatility or supply/demand mismatch; this is called slippage and is an important input to backtesting to get a true picture of your strategy.
- **Position Sizing: **  This refers to the size of the position that your overall portfolio will be invested into; this helps you choose which assets to choose and how much risk you take on an overall basis. 
- **Performance Evaluation: ** Maybe you had 100% return in an X time period, but your robot could have lost 100% money in some instances as well, then that is not a good robot/strategy; you need to also evaluate how it fits in with your risk profile. 

#### Step 3: Optimization of Your Strategy

Your backtesting results will give you a lot of insight into what works and what does not work; you should stress-test your strategy to see how it works in varied market conditions and optimize it accordingly in the live environment. 

- **Adjusting for Stop Losses/ Slippages/ Profit Margins/Position Sizing: ** , E.g., you had a 1.5% stop loss coded in your strategy, which gave you a 10% return, you can try maximizing or minimizing this number to see what is an optimal fit depending on your risk profile. 
- **In and Out of Sample Testing: **While optimizing, you should maintain a sample time frame which you are using to optimize your returns and then test that optimized strategy on out of sample time period to ensure you are not overfitting the curve where your strategy only works in one time period but performs poorly in others. 

#### Step 4: Execution of Your Strategy

Finally, the exciting bit, going live after all your hard work to mint some money. 🤑

- **Broker Selection: ** Choosing a broker with reliable API services to execute orders programmatically. 
- **Virtual Private Servers: ** You can't run a serious strategy on your personal laptop from your home internet network. What if you have an open leveraged position and suddenly your internet goes down, and your code stops working to make losses. Not ideal, so you need to deploy your code to a VPS, preferably near the Stock Exchange servers, to get faster execution time.

#### Step 5: Evaluation of Your Strategy

After you have executed your strategy into live markets, you will have to constantly evaluate with the strategy is still relevant with the current market conditions or if any tweaks are required to make it perform better because frankly, no one strategy can work forever, sooner or later, conditions change, and you are out of business. 

#### Conclusion:

And that's it; these are the 5 steps that I think you should really understand when you have a strategy in mind but want to do algorithmic trading. Creating an algo is a tough thing to do and involves many thoughts and testing, probably why Quants are paid big money in asset management firms and hedge funds. 

What do you think about the article? Appreciate your comments below or to me personally on [Twitter](https://twitter.com/yash_roongta)  or [Linkedin.](https://uk.linkedin.com/in/yashroongta)  

> Do you have any exciting strategies to build but still unsure how to go about it? Reach out to me, and I will try my best to help you. 

If you like it up till now, consider buying me a coffee ☕ by  [clicking here](https://www.buymeacoffee.com/tradewithyash)  or the button below.

%%[buymeacoffee-btn]

##### Credits:
- Algo Trading 101
- Investopedia
- Photo by <a href="https://unsplash.com/@austindistel?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Austin Distel</a> on <a href="/s/photos/trading?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  