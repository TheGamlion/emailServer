import os 
import smtplib
import csv
from datetime import date
from email.message import EmailMessage

EMAIL_ADRESS = os.environ.get('GMAIL_ADRESS')
EMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'Wetter' + str(date.today())
msg['From'] = EMAIL_ADRESS
msg['To'] = 'thegamlion@gmail.com'



body = ""
with open('wetter.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x in reader:
        print(str(x))
        body = body.join(','+ str(x))
        body = body.join('\n')

print(body)
    
msg.set_content("test")


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)