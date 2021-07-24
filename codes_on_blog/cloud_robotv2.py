from jugaad_data.nse import NSELive
import telegram_send as ts
import time

def get_prices(stockSymbol):
    
    n = NSELive()
    q = n.stock_quote(stockSymbol)
    return q['priceInfo']['lastPrice']

def send_telegram_message(message):
    ts.send(messages = [str(message)])

live_prices = []
count = 0

while True: 
    current_price = get_prices('HDFC')
    live_prices.append(current_price)
    count = count + 1
    print(f'{count} Minutes Done')

    if len(live_prices) == 5:
        avg_price = round((sum(live_prices[-5:])/len(live_prices[-5:])),2)
        if count == 5:
            send_telegram_message(f'The Average Price of HDFC For Last 5 Minutes is {avg_price}')
            #print(f'The Average Price of HDFC For Last 5 Minutes is {avg_price}')
            count = 0
            live_prices.clear()
    
    time.sleep(60)

    