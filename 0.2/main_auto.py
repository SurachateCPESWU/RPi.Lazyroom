import psutil
from subprocess import Popen
import MySQLdb
import os

host=""
user=""
passwd=""
dbname=""
db=MySQLdb.connect(host,user,passwd,dbname)
cursor=db.cursor()


def TURN_ON(name):
  sql="UPDATE `DEVICE` SET `Status` = True WHERE Name =\'%s\'"%name
  cursor.execute(sql)
  db.commit()
  return "ok"

Popen(['python', '/home/pi/Desktop/lazyroom/AUTO.py'])
TURN_ON("MAIN_AUTO")
