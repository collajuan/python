import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": '...'
    }
url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=UC4CBLQNXJQBCLA4"
r = requests.get(STOCK_ENDPOINT, params=parameters)
r.raise_for_status()
data = r.json()

data_list = [value for (key, value) in data['Time Series (Daily)'].items()]
yesterday_close = float(data_list[0]["4. close"])
daybefore_yesterday_close = float(data_list[1]["4. close"])
print(yesterday_close,daybefore_yesterday_close)
positive_difference = abs(yesterday_close-daybefore_yesterday_close)
print(positive_difference)
percentage_difference = (1-yesterday_close/daybefore_yesterday_close)*100
print(percentage_difference)

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if percentage_difference > 5:
    response = requests.get(NEWS_ENDPOINT, params={
        'q':COMPANY_NAME,
        'from':'2024-12-31',
        "language":'en',
        'apiKey':'...'
    })
    response.raise_for_status()
    print(response.json())
    news_data = response.json()["articles"]
#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    firts_articles = news_data[:3]


#Create a new list of the first 3 article's headline and description using list comprehension.
    list_to_send = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in firts_articles]
    print(list_to_send)
#Send each article as a separate message via Twilio. 
    if yesterday_close > daybefore_yesterday_close: body_message = f"TESLA🔺{percentage_difference}%"
    else: body_message = f"TESLA🔻{percentage_difference}%"

    for article in list_to_send:
        client = Client("...", "...")
        message = client.messages.create(
            body=body_message + article,
            from_='+...',
            to='+...'
        )

        print(message.status)





