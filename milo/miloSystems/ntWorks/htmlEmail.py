#!/usr/bin/python

import smtplib

def send_htmlemail(sender, receivers):
    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: SMTP HTML e-mail test
    
    This is an e-mail message to be sent in HTML format
    
    <b>This is HTML message.</b>
    <h1>This is headline.</h1>
    """

    try:
       # smtpObj = smtplib.SMTP('localhost')
       smtpObj = smtplib.SMTP('mail.your-domain.com', 25)
       smtpObj.sendmail(sender, receivers, message)
       print("Successfully sent email")
    except SMTPException:
       print("Error: unable to send email")