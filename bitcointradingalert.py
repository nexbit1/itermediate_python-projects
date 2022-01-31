import requests
from datetime import datetime, timedelta
from smtplib import SMTP
import os

# now = datetime.today().isoformat()
# yesterday = (datetime.today() - timedelta(days=1)).isoformat()


email = 'enter mail' #check smtp
password = 'password'
API_KEY = os.environ.get('API_KEY')  #hidden in local environment
headers = {'X-CoinAPI-Key': API_KEY}

def get_crypto_price(crypto, fiat):
    url = f'https://rest.coinapi.io/v1/exchangerate/{crypto}/{fiat}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()['rate']
    return (round(data, 3))

def get_24hrs_updown(crypto, fiat):      #apiwesbite = https://www.coinapi.io/    #time_start = {yesterday} and time_end ={now} to change automatically
    url1 = f'https://rest.coinapi.io/v1/exchangerate/{crypto}/{fiat}/history?period_id=1DAY&time_start=2022-01-30T00:00:00&time_end=2022-01-31T00:00:00'
    response = requests.get(url=url1, headers=headers)
    response.raise_for_status()
    data = response.json()
    rate_high_today = data[0]['rate_high']
    rate_high_yesterday = data[1]['rate_high']
    x = rate_high_today - rate_high_yesterday
    return abs(x)

news_api = os.environ.get('news_api')
def get_news():   #news_api = https://newsapi.org/
    url = f'https://newsapi.org/v2/everything?q=bitcoin&from=2022-01-20&sortBy=publishedAt&apiKey={news_api}'
    response = requests.get(url=url)
    response.raise_for_status()
    data = response.json()['articles']
    articles_3 = data[:3]
    formated_articles = [f'Headline:{article["title"]}\n\n Brief:{article["description"]}' for article in articles_3]
    return formated_articles

if get_24hrs_updown(crypto='BTC', fiat='USD') > 400:
    list_of_articles = [i for i in get_news()]
    with SMTP('smtp.mail.yahoo.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        for i in list_of_articles:

            connection.sendmail(
                from_addr=email,
                to_addrs='reciver mail',
                msg=f"Subject:Bitcoin: {get_crypto_price(crypto='BTC', fiat='USD')}$\n\n {i.encode()} ")
                #i.encode doesnt give readable data but is able to send email gives error when done in utf_8 format




