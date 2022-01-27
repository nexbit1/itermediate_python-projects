from smtplib import SMTP
from datetime import datetime
import random

email = 'omkar7656@yahoo.com'
password = 'ugajedqsxqkvseez'

with open('quotes.txt') as data:
     x = data.readlines()

now = datetime.now()

with SMTP('smtp.mail.yahoo.com') as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    if now.hour == 11:
        connection.sendmail(
            from_addr=email,
            to_addrs='omkaratagnel@gmail.com',
            msg=f'Subject:Anime quotes\n\n {random.choice(x)}')




