# Configure your gmail account and setup 2 factor athentication
# generate app password: collect the information and put it on another file e-mail_sender_password.py for security reasons

# create a function to send emails
# for the receiver we are going to create a temporary email address with temp-mail.org
# kifimeb197@jthoven.com

from email.message import EmailMessage
from password import password
import ssl
import smtplib


email_sender= "Your email address"
email_password = password

email_receiver = "kifimeb197@jthoven.com"   # this is just a temporary email address

subject= "Write the subject of the mail"

body = "Please write the text you want to send on your email"

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)   # Used for login
    smtp.sendmail(email_sender, email_receiver, em.as_string()) 
