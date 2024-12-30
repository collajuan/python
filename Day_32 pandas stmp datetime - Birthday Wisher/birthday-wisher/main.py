##################### Hard Starting Project ######################
import pandas
from datetime import  datetime
import random
import smtplib

MY_EMAIL = "collajuan@hotmail.com"
PASSWORD = ""

today = (datetime.now().month, datetime.now().day)
birthay_data = pandas.read_csv("birthdays.csv")
birthay_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthay_data.iterrows()}

if today in birthay_dict:
    birthay_person = birthay_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,2)}.txt"
    with open(file_path) as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", birthay_person["name"])
    # Envia email
    # with smtplib.SMTP("smtp-mail.outlook.com") as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL, password=PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=birthay_person["email"],
    #         msg=f"Subject:Happy Birthday\n\n{letter}"
    #     )
    # Prueba generando txt
    with open(f"letter_templates/letter{birthay_person["name"]}_.txt", "w") as new_letter:
        new_letter.write(letter)


