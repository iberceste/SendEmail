import smtplib
import datetime as dt
import random
import pandas


my_email = "ipekkunluupy@gmail.com"
password = "your_password"
now = dt.datetime.now()
day = now.weekday()

with open("quotes.txt") as f:
    lines = f.readlines()
    choose_quote = random.choice(lines)

if day == 3: #You can change it to any day you want
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Daily Quote\n\n{choose_quote}")
        connection.close()




