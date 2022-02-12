import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

user = ''
password = ''
receiver = ''

target_price = float(input('Enter target price: '))

url = 'https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5WJD1C/ref=sr_1_4?crid=2VPTA4NS32D56&keywords=iphone%2B12&qid=1644671812&sprefix=iphone%2B12%2Caps%2C345&sr=8-4&th=1'
header = {
    'Request Line': 'GET / HTTP/1.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36'
}
response = requests.get(url=url, headers=header)


soup = BeautifulSoup(response.text, 'lxml')  #pycharm has inbuilt lxml parser😁
price = soup.find(class_='a-offscreen').get_text()
price_without_currency = price.split('₹')[1]
price_without_comma = price_without_currency.replace(',', '')
price1 =float(price_without_comma)


if target_price > price1:
    with SMTP('smtp.mail.yahoo.com') as console:
        console.starttls()
        console.login(user=user, password=password)
        console.sendmail(from_addr=user,
                         to_addrs=receiver,
                         msg=f'SUBJECT:iPhone 12 PRICE ALERT!!!\n\niPhone 12 selling at {price1}\nGo sell kidney !!!')



