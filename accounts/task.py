import re
import smtplib
from tabulate import tabulate
from email.utils import formatdate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from runtime_business.settings import *


def SendEmailToSales(send_to, email, sale_password):
    username = email_username
    password = email_password
    send_from = 'runtimeterrorapi@gmail.com'
    Cc = ''
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Cc'] = Cc
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = 'Sales Login Details'
    body = f'YOUR LOGIN DETAILS ARE AS FOLLOW'
    body = MIMEText(body)
    msg.attach(body)
    head = ['EMAIL', 'PASSWORD']
    Email = str(email)
    Password = str(sale_password)
    mydata = [[Email, Password]]
    table = tabulate(mydata, headers=head, tablefmt='html')
    table = re.sub(
     r'<table([^>]*)>',
     r'<table\1 table align="center" border="2" cellspacing="2" cellpadding="2">',
     table
    )
    msg.attach(MIMEText(table, "html"))
    smtp = smtplib.SMTP('smtp.gmail.com', '587')
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
    return None


def SendEmail(send_to, meeting_url, meeting_password):
    username = email_username
    password = email_password
    send_from = 'developers.lbyspace@gmail.com'
    Cc = ''
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Cc'] = Cc
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = 'Meeting'
    body = f'Your booking is  '
    body = MIMEText(body)
    msg.attach(body)
    head = ['Meeting_link', 'Password']
    Meeting_link = str(meeting_url)
    Meeting_Password = str(meeting_password)
    mydata = [[Meeting_link, Meeting_Password]]
    table = tabulate(mydata, headers=head, tablefmt='html')
    table = re.sub(
     r'<table([^>]*)>',
     r'<table\1 table align="center" border="2" cellspacing="2" cellpadding="2">',
     table
    )
    msg.attach(MIMEText(table, "html"))
    smtp = smtplib.SMTP('smtp.gmail.com', '587')
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
    return None