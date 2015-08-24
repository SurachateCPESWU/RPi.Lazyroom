import RPi.GPIO as GPIO

class setdevice:
	def __init__(self,name,status,pin):
		self.name=name
		self.status=status
		self.pin=pin

	def show_info(self):
		print self.status
		print self.pin

###############################
PIN=["","","",""]
PIN[0]=35
PIN[1]=36
PIN[2]=37
PIN[3]=38
###############################
GPIO.setmode(GPIO.BOARD)
for i in range(1,5):
        temp=PIN[i-1]
        GPIO.setup(temp,GPIO.OUT)
        GPIO.output(temp,0)
        globals()['DEVICE%d'%i]=setdevice("DEVICE%d"%i,False,temp)

def TURN_ON(name):
	if name.status==False:
		GPIO.output(name.pin,1)
		name.status=True
		return "%s is On"%name.name
	elif name.status==True:
		return "%s is on"%name.name

def TURN_OFF(name):
	if name.status==True:
		GPIO.output(name.pin,0)
		name.status=False
		return "%s is off"%name.name
	elif name.status==False:
		return "%s is off"%name.name
