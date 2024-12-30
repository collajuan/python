import smtplib
import datetime as dt
import random

my_email = "collajuan@hotmail.com"
password = ""

with open("quotes.txt") as file_data:
    quotes_list = file_data.readlines()

weekday = dt.datetime.now().weekday()
random_quote = random.choice(quotes_list)
# with smtplib.SMTP("smtp-mail.outlook.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="collajuan@gmail.com",
#         msg=f"Subject:Hola\n\n{random_quote}"
#     )


