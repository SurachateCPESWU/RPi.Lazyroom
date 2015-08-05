import os
import time

ip=""

os.system("gpio mode 26 out")

if os.system("ping -c 1 %s"%ip)== 0 :
	os.system("gpio write 26 0")
	temp = 0
else :
	os.system("gpio write 26 1")
	temp = 256

while 1:
       #########COMPUTER STATUS###########
       now = os.system("ping -c 1 %s"%ip)

       if((now==0) and (now != temp)):
           os.system("gpio write 26 0")
           temp = 0
       elif((now==256) and (now != temp)):
           os.system("gpio write 26 1")
           temp = 256
       time.sleep(1)
