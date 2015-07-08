import MySQLdb
import time
import os
import RPi.GPIO as GPIO
from config import *

def Get_POWER():
  sql="SELECT * FROM `DEVICE` WHERE NAME=\"POWER\""
  cursor.execute(sql)
  PIN_POWER=cursor.fetchall()
  return PIN_POWER[0][0]

def Change_STATUS():
  sql="UPDATE `ALARM` SET `ACTIVE`=0 WHERE NAME='%s'"%TIME_ALARM[0][0]
  cursor.execute(sql)
  db.commit()

def TURN_ON(name):
  sql="SELECT * FROM `DEVICE` WHERE Name=\'%s\'"%name
  cursor.execute(sql)
  temp=cursor.fetchall()
  if temp[0][2]==0:
    os.system("gpio write %d 0"%temp[0][0])
    sql="UPDATE `DEVICE` SET `Status` = True WHERE Name =\'%s\'"%name
    cursor.execute(sql)
    db.commit()
    return "ok"
  else : return "ERROR"

##########Check active############
db=MySQLdb.connect(host,user,passwd,dbname)
cursor=db.cursor()
sql="SELECT * FROM `ALARM` WHERE ACTIVE=1"
cursor.execute(sql)
TIME_ALARM=cursor.fetchall()
NUM_ALARM=len(TIME_ALARM)

if(NUM_ALARM>=1):
    #################################
    PIN_POWER=Get_POWER()
    #################################
    while 1:
       #########COMPUTER STATUS###########
       if os.system("ping -c 3 %s"%ip)== 0 :
           print("%s is Online"%ip)
           com_status=1
       else :
           print("%s is Offline"%ip)
           com_status=0

       ##############MAIN#################
           
       if time.strftime("%H%M") == TIME_ALARM[0][0] and  com_status == 0 :
        print("START")
        os.system("gpio write %d 0"%PIN_POWER)
        time.sleep(1)
        TURN_ON("DEVICE1")
        os.system("gpio write %d 1"%PIN_POWER)
        time.sleep(20)
        os.system("cvlc ./media/music ./media/go.mp4 vlc://quit")
        print("START YOU COMPUTER")
        break
       else :
        print("ERROR")

       ####################################
       time.sleep(60)
else:
  print "Don't have alarm"
