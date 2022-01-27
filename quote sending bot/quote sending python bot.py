from smtplib import SMTP
from datetime import datetime
import random

email = 'testemail@yahoo.com'
password = ''

with open('quotes.txt') as data:
     x = data.readlines()

now = datetime.now()

with SMTP('smtp.mail.yahoo.com') as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    if now.hour == 11:
        connection.sendmail(
            from_addr=email,
            to_addrs='testemail@gmail.com',
            msg=f'Subject:Motivational quotes\n\n {random.choice(x)}')




