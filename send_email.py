import os
import smtplib
import ssl

# this doesn't work, need to put working email and password info in
EMAIL = "FAKE@GMAIL.COM"


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = EMAIL
    password = os.getenv("PASSWORD")
    receiver = EMAIL
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
