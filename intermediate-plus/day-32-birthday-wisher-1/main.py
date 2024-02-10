import smtplib
import datetime as dt
import random

#Select random quote

with open("quotes.txt") as quotes_file:
    quotes_str = quotes_file.readlines()
    quotes_list = quotes_str.split("\n")

quote = random.choice(quotes_list)

#Date time

now = dt.datetime.now()
month = now.month
day = now.day
weekday = now.weekday

#Send quote

g_email = "jake2ndary@gmail.com"
y_email = "jake2ndary@yahoo.com"
password ="tebkdbxicshfhaaf"



with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
    connection.starttls()
    connection.login(user=g_email, password=password)

    if weekday == 0:
        connection.sendmail(
            from_addr=g_email,
            to_addrs=y_email,
            msg=f"Subject:Monday {month}/{day} Quote\n\n{quote}"
        )


# date_of_birth = dt.datetime(year=1992, month=1, day=7, hour=4)
# print(date_of_birth)
