import requests
from datetime import datetime
from smtplib import SMTP
import time

MY_LAT = float(input('Your latitude: '))    #FIND FROM HERE( https://www.latlong.net/)
MY_LNG = float(input('Your longitude: '))

email = input('you\'re email: ')            #turn the security settings off
password = input('you\'re password: ')
reciever = input('enter email of the reciever: ')

parameters = {
    'formatted': 0   #to set to 24hr format in sunrise,sunset api
             }
def iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json') #(API LINK:http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
    response.raise_for_status()
    data1 = response.json()
    iss_longitude = float(data1["iss_position"]["longitude"])
    iss_latitude = float(data1["iss_position"]["latitude"])

    #checking if iss location within +-5 range of my locaton
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5)  and (MY_LNG - 5 <= iss_longitude <= MY_LNG + 5):
        return True

def is_dark():
    response = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)  #(API SITE: https://sunrise-sunset.org/api)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour
    #checking if its dark in the sky
    if time_now >= sunset and time_now <= sunrise:
        return True

while True:   #infinite loop updates evry 1 minute   #(RUN IN CLOUD : https://www.pythonanywhere.com/registration/register/beginner/ )
    time.sleep(60)
    if is_dark() and iss_overhead():
        with SMTP('smtp.mail.yahoo.com') as connection:  #yahoo: smtp.mail.yahoo.com #gmail: smtp.gmail.com
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs= reciever,
                msg='Subject:Look up in the sky👆🏻\n\n ISS station hovering in the sky over the sky')


