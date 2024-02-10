##################### Extra Hard Starting Project ######################

import pandas as pd
import datetime as dt
import random
import smtplib

g_email = "jake2ndary@gmail.com"
y_email = "jake2ndary@yahoo.com"
password ="tebkdbxicshfhaaf"

receipients = {}

# 1. Update the birthdays.csv

bday_df = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv

todays_date = dt.date.today()
todays_month = todays_date.month
todays_day = todays_date.day

for ind in bday_df.index:
    birth_month = bday_df['month'][ind]
    birth_day = bday_df['day'][ind]
    name = bday_df['name'][ind]
    email = bday_df['email'][ind]
    if birth_month == todays_month and birth_day == todays_day:
        receipients[name] = email

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

with open("letter_templates/letter_1.txt") as letter_1_file:
    letter_1 = letter_1_file.read()
with open("letter_templates/letter_2.txt") as letter_2_file:
    letter_2 = letter_2_file.read()
with open("letter_templates/letter_1.txt") as letter_3_file:
    letter_3 = letter_3_file.read()
letter_list = [letter_1, letter_2, letter_3]

if len(receipients) > 0:
    for name in receipients:
        personal_letter = random.choice(letter_list)
        personal_letter = personal_letter.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=g_email, password=password)
            connection.sendmail(
                from_addr=g_email,
                to_addrs=g_email,
                msg=f"Subject:Happy Birthday!"
                    f"\n\n{personal_letter}"
            )

# 4. Send the letter generated in step 3 to that person's email address.




