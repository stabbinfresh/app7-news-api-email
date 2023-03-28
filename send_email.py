import os
import smtplib
import ssl

EMAIL = "apptestemail31@gmail.com"


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
