#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

##gmail/usr/password
             #usr, passwrd, to,txt for sending!
def sendmail(usr, passwrd, to, txt):
  msg = MIMEMultipart()

  msg['From'] = usr
  msg['To'] = to
  msg['Subject'] = ''
  
  msg.attach(MIMEText(txt))

  mailServer = smtplib.SMTP('smtp.gmail.com', 587)
  mailServer.ehlo()
  mailServer.starttls()
  mailServer.ehlo()
  mailServer.login(usr, passwrd)
  mailServer.sendmail(usr,to,msg.as_string())
  mailServer.close()
