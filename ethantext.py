import email
import smtplib
import ssl
from scheduleReader import scheduleReader.numbers, scheduleReader.dates, scheduleReader.type scheduleReader.email, scheduleReader.password


## define variables
number = scheduleReader.numbers
service = scheduleReader.type
date = scheduleReader.dates
sender = scheduleReader.email
password = scheduleReader.password
for i in range(len(numbers)):
    recipient = f"{number[i]}@vtext.com"

    ## define the message/text
    msg: str = f"""\
    To: {recipient}
    Subject: Dobrindt Landscape Services
    \n
    You have an upcoming {service[i]} on {date[i]}"""

    ## defining the server and port, and creating SSL context
    server = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    ## send the email/text
    try:
            with smtplib.SMTP_SSL(server, port, context=context) as email:
                    email.login(sender, password)
                    email.sendmail(sender, recipient, msg)
            print("Text sent successfully")
    except:
            print("Something went wrong- text not sent")
