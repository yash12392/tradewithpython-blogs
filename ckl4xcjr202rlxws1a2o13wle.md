## Can an average Retail Investor really do High Frequency Trading (HFT) using Python?

Hi There! 😄

If you have dabbled upon reading this article, you are probably one of us! Who? You ask.
A community of believers who have thought of getting into High-Frequency Trading (HFT) independently or that you have the potential to beat the Institutional Investors (like the GameStop Saga) or make millions in HFT just sitting out of your room. 

**I don't blame you,** that side of the world is indeed fancy where you are spending some time on the beach 🏖️ sipping beer deciding which country/city to go next while the computers are making money for you in the background. 

*Now, if you are someone who has heard the acronym "HFT" multiple times but still doesn't understand what it means in practice, here is a short 11 min video clip for you that I like. The video also talks about quote-stuffing and spoofing, which are generally illegal in the markets.*

%[https://www.youtube.com/watch?v=z4nCTdQlH8w]

> Now that you know what HFT is, you now know that "Latency" matters a lot. In short, every Millisecond counts. 🏃‍♂️

#### So let's get to the point, can an average retailer investor (like you and me) pull off High-Frequency Trading from the comfort of their home using Python?

#####  ***I am afraid not.***

Here are a couple of barriers to entry for retail investors:

- **Lack of Technical Infrastructure:** Running your algorithms on average laptops or average virtual private servers will introduce a lot of latency. Think of below as a simple example of opening up a Youtube video on your browser and waiting for it to load. You waited 1.7 s for this to complete; in this time, someone out there might have completed 100s of trades already. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1613232744810/5Hb-jjSYB.png)
(Source:  [KeyCDN](https://www.keycdn.com/support/what-is-latency))

- **Access to Data:** Getting "Tick" Level data in the fastest manner possible. A "Tick" is a measure of the minimum upward and downward movement in the security price. Most of the stockbrokers worldwide provide "1minute" data, a minute could have as many as 60-70 ticks in very high volume sessions. 

- **Expensive Co-Locations:** When trading, ultimately, your orders will have to be sent to the exchange to execute, and since you want your orders to be executed before anyone else, you would like to set up shop near an exchange, so there is minimum latency. It can be costly depending on which exchange we are talking about. 

- **Increased Burden of Compliance:** Depending on the country you are in, there will be different regulations around HFT. Still, there is generally increased scrutiny on your trades, and the requirement to disclose the 1000s of transactions you make during your Income Tax returns can be onerous. 

**Hey Yash, What does Python have to do with HFT, and why can't I use it? 
Glad you asked! 😆**

Python is a high-level programming language with its tradeoffs; for the benefit of making it easy and understandable for everyone, compromises on speed/efficiency/memory use have been made. Some specific reasons:

- With HFT, you will be dealing with terabytes of data as you collect every tick; with Python, it's complicated to manage memory.

- Python also takes a beating when it comes to latency and speed; if any other trader out there can calculate those numbers faster than you, you are out of luck! For latency-sensitive strategies, large enterprises like Goldman Sachs/ JP Morgan would go for `C++`.

*On a side note, an article by the Financial Times from 2013 telling you how every millisecond counts for HFT focused firms. Click  [here](https://www.ft.com/content/2bf37898-b775-11e2-841e-00144feabdc0)  to read.*

To end this article, if you are an average retail investor who is planning to build strategies that depend on milliseconds of data, I highly doubt you will be able to pull it off without a significant amount of cost. If you can spend that amount of money, you are not an average retail investor. 🙂

Do let me know in the comments what you think of this article and if you had like me to cover any other points. All constructive criticism is welcome. 😎

If you liked this article, consider buying me a coffee ☕ by  [clicking here](https://www.buymeacoffee.com/tradewithyash)  or the button below.

%%[buymeacoffee-btn]