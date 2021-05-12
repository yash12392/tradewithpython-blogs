## API, SDK, WebSockets & List of Brokers in India That Support Algo Trading

Hi There 😇, **Algo-Trading** is just picking up in India. Almost every discount/traditional brokerage house wants to grab this market by offering innovative products and robust APIs for order executions, market feeds, etc.

This has led to a boom in the number of broking firms offering their API services. This article aims to cover most brokers in India offering this service and give you a comprehensive view of what they offer and how they can be of use to you.

> But before we get started, you need to understand some methodology related to this topic; you might have read the technical version of each word below, but here is my attempt to explain this from a Finance point of view.

### API (Application Programming Interface)

Let's think of a traditional bank like **State Bank of India**, you walk into any branch over the country, and you see multiple desks within the branch. For a minute, think of these desks as a gateway, your gateway to access new financial products or conduct transactions. You need to deposit money, sure go to bank teller gateway; you need to enable online banking, go to support gateway, similarly, you need to open a safe deposit box, you go to that relevant gateway within the bank.
All these gateways are just endpoints that you need to call to access information or post information to them. Yes, that's an API. **Very, very simple.
You do not need to anything more.**

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1619412439693/kUIXFpHW7.png)
*Technical Representation of an API on how it act's as a gateway. *
Source:  [Medium](https://medium.com/@perrysetgo/what-exactly-is-an-api-69f36968a41f) 

### SDKs (Software Development Kits)

An **SDK** in technical terms serves as a wrapper around an **API**, what this means is, an API is just a gateway, BUT, an SDK is a tool that contains all the various gateway and can easily be used by developers for use in their code/software.

In real life, think of a Relationship Manager (RM) from SBI (considering you have the luxury of having one RM), this RM acts as an SDK for you, you need any help related to the bank, you deal with the SDK who in turn would deal with all the API gateways.

SDK is available in multiple languages like **Python, Go, Rust, PHP, .NET**, it depends on the broking house on which languages they prefer for their clients. You are also always welcome to create your own SDK in any language you want. 

### WebSockets

You might have heard of the word **Ticker Tape** which was an actual thing in the 1990s; the stock prices would be printed on this tape and would be streamed to all brokers who had a subscription.  It used to look something like this. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1619847932254/7jg0I4V6E.png)
Source:  [Pinterest](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F228909593531509373%2F&psig=AOvVaw2st4SvHt1NWLwJ6gd75-XK&ust=1619934133227000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOjYy4fjp_ACFQAAAAAdAAAAABAD) 

**Websockets** is just a digital version of **Ticker Tapes**; a WebSocket is basically a connection between us and the broker servers where we request the continuous stock prices information to the server, and it responds with a continuous stream of prices until the broker or client stops the connection. 

Most of the Algo-Trading strategies would rely on live stock prices and use WebSockets to get that live prices stream and use it to satisfy their strategy conditions and place orders. If a particular broker does not provide a WebSocket feed, you will have to arrange your own feed to run strategies which can be very inconvenient and expensive. 

### List Of Brokers with APIs

> Before the list, Disclaimer: I do not work for any broking entities mentioned below, and nor is this any recommendation or affiliate marketing. This information is for your reference purpose only. 
>> Every Broker Name below is hyperlinked to the relevant API page, and there is no monetary benefit to Trade With Python.

Just so you know, the table is scrollable horizontally, some columns might be hidden based on your screen size.

| Broker | API| SDKs | Websockets | Charges|
| ------    |    ------   |  ------ | ------ |  ------ |
| [5Paisa](https://www.5paisa.com/developerapi)| `Trading API` | `Python` <br/>`NodeJS` <br/> `Go` | No | Nil |
|  [Abstox](https://www.abstox.com/) <sup>1</sup> | `Trading API` <br/>  `Market Data API`   | None  | Yes | Nil |
|  [AliceBlue](https://antplus.aliceblueonline.com/#introduction) | `Trading API` | `Python` | Yes | Nil |
|  [AngelBroking ](https://smartapi.angelbroking.com/docs)  | `Publisher API`<br/> `Trading API` <br/> `Market Feeds API` <br/> `Historical Data API` | `Python` <br/> `Java` <br/> `NodeJS` <br/> `R` <br/> `Go` | Yes | Nil |
|  [Composite Edge](https://www.compositedge.com/compositedge-api) <sup>1</sup> | `Trading API` <br/>  `Market Data API`  | None  | Yes | Nil |
|  [Fyers](https://fyers.in/fyers-api/) <sup>2</sup> | `Trading API` <br/>  `Market Data API`  | `Python` <br/> `NodeJS`| Yes | Nil |
|  [ICICI Securities](https://api.icicidirect.com/apiuser/ICICIDirectAPIDOC.htm#sec-Overview)  | `Trading API` | None | No | Nil |
|  [Kotak Securities](https://preferred.kotaksecurities.com/landing-page/api/)  | `Trading API` | `Python` | No | Nil |
|  [MasterTrust](https://www.mastertrust.co.in/product-trading-api) <sup>3</sup> | `Trading API` | `Python`<br/> `NodeJS` | No | Nil |
|  [SS Corporate Securities](https://www.sscorporate.com/next-gen-trading-api/api.html) <sup>1</sup> | `Trading API` <br/> `Market Data API` | None | Yes | Nil |
|  [Trade Smart ](https://tradesmartonline.in/products/swing-api/) | `Trading API` | None | No | Nil |
|  [TrustLine](https://www.trustline.in/TrustlineAPIdocs.html) <sup>4</sup> | `Trading API` | None | No | Nil |
|  [Upstox](https://upstox.com/developer/) <sup>5<sup> | `Trading API` <br/> `Historical Data API` | `Python` <br/> `NodeJS` | Yes |  `750 INR` <br/> `500 INR`|
|  [Zebu](https://zebull.in/#/zebullDoc/intro)  | `Trading API` | None | No | Nil |
|  [Zerodha](https://kite.trade/)  | `Trading API` <br/> `Historical Data API` | `Python` <br/> `Java` <br/> `PHP` <br/> `NodeJS` <br/> `C#` <br/> `.NET` <br/> `Go` <br/> `Rust` <br/> `C++`| Yes | `2000 INR` <br/> `2000 INR` |
|  [ShareKhan](https://www.sharekhan.com/active-trader/oalert/api-integration)  | `Trading API` | None | No | Nil |
|  [TradeJini](https://arrow.tradejini.com/)  | `Trading API` | None | No | Nil |
|  [Samco ](https://developers.stocknote.com/api/#stocknote-api-documentation) | `Trading API` | `Python` <br/> `Java` <br/> `NodeJS` | Yes | Nil |
|  [IIFL Securities](https://api.iiflsecurities.com/landing-page.html)  | `Trading API` | `Python` <br/> `NodeJS` <br/> `PHP` <br/> `Rust` <br/> `C#` <br/> `Java` <br/> `VB.Net` | No | Nil |

**[1]:** The broker is utilizing  [Symphony Fintech APIs](https://symphonyfintech.com/xtsapi/)  
**[2]:** Fyers provide Historical/Websocket Market Data API via TrueData vendor, which has a subscription fee.  
**[3]:** MasterTrust website mentions they have SDKs, but I couldn't find them. TradeLab has developed its API  
**[4]:** API developed by TradeLab  
**[5]:** Upstox API currently under Beta Development

### List of Brokers with no API but that support Algo Trading via 3rd Party Platforms

A few days back, I wrote about the **low-code/no-code trading platforms in India** which give retail investors the power to create/backtest/deploy their strategies without any knowledge of coding. All of the above brokers (who have APIs) are supported by at least one low-code platform mentioned in that article which you can  [read here. ](https://tradewithpython.com/list-of-low-codeno-code-algorithmic-trading-platforms-in-india) 

The below list of brokers do not have their open APIs, but if you have an account with them, they still allow you to Algo Trade using  [TradeTron.](https://tradetron.tech/) They might be supported by other low-code platforms as well, please feel free to mention them in the comments, and I will update the article.

1.  [Acumen Group](https://acumengroup.in/) 
2.  [Aditya Birla Money](https://stocksandsecurities.adityabirlacapital.com/) 
3.  [Arham Share](https://www.arhamshare.com/) 
4.  [Arham Wealth](https://www.arhamwealth.com/) 
5.  [Arihant](https://www.arihantcapital.com/) 
6.  [Basan](https://basanonline.com/) 
7.  [Enrich Broking](https://enrichbroking.in/) 
8.  [Gill Broking](https://www.gillbroking.com/) 
9.  [Goodwill Wealth Management](https://gwcindia.in/) 
10.  [Share India](https://www.shareindia.com/) 
11.  [Motilal Oswal](https://www.motilaloswal.com/) 
12.  [Nirmal Bang](https://www.nirmalbang.com/) 
13.  [Prabhudas Liladher](https://www.plindia.com/)
14.  [Profit Mart](https://profitmart.in/) 
15.  [Rudra Shares](https://www.rudrashares.com/) 
16.  [Swastika](https://www.swastika.co.in/) 
17.  [Trade Swift](https://www.tradeswift.net/) 
18.  [Wisdom Capital](https://wisdomcapital.in/) 

**That's it, Folks** ✅ I spent a significant time researching and collating information for this article. Apologies in advance if there are any factual errors within the article, but I would be grateful if you can point them out in the comments below or using the Contact Us page on this blog.

> If you run a brokerage house and also provide Algo-Trading service, do give me a shout, and I will be more than happy to add you to this article. 😃

Again, I would be more than happy to listen to you on some **feedback **and any ideas on future articles/content; I thank you for being a reader of TradeWithPython.
If you haven't subscribed to the **newsletter **already, you can do so by putting in your email at the top of this blog, and you will receive all notifications about my future articles. (No spam!)

To support me for all the effort to create this content, consider buying me a coffee ☕ by  [clicking here ](https://www.buymeacoffee.com/tradewithyash) or the button below.

%%[buymeacoffee-btn]



