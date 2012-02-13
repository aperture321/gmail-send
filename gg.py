#!/usr/bin/python

import poplib
from email import parser


def login(us,pw):
  pop_conn = poplib.POP3_SSL("pop.gmail.com")
  pop_conn.user('recent:'+us)
  pop_conn.pass_(pw)
  return pop_conn

def getmsg(us,pw): #Get messages from server
  pop_conn = login(us,pw) 
  messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
  # Concat message pieces:
  messages = ["\n".join(mssg[1]) for mssg in messages]
  #Parse message into an email object:
  value = [parser.Parser().parsestr(mssg) for mssg in messages]
  quiter() #need to logout to reupdate message mail 
  return value

def messageretrieve(oldy,number,us,pw):
  messages = getmsg(us,pw)
  new = messages[-1]['From']
  if number in messages[-1]['From']: ##Returns true if your phone number is in there
    oldnew = messages[-1].get_payload()
    if oldnew != oldy: #if it wasn't the same message
      return oldnew
  return oldy

def quiter():
  pop_conn.quit()
