import RPi.GPIO as GPIO
import threading
import time

global GPIOLampGroen
global GPIOLampOranje
global GPIOLampRood

global GPIOKnop1
global GPIOKnop2
global GPIOKnop3
global GPIOKnop4

# Settings
# -- Lampen GPIO
GPIOLampGroen = 7
GPIOLampOranje = 11
GPIOLampRood = 13

# -- Knoppen GPIO
GPIOKnop1 = 29
GPIOKnop2 = 31
GPIOKnop3 = 33
GPIOKnop4 = 35

# Einde settings

# status = 0 -- Lamp uit, status = 1 -- Lamp Aan
GPIO.setup(GPIOKnop1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIOKnop2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIOKnop3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIOKnop4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

lamp_status = [[GPIOLampGroen,0],[GPIOLampOranje,0],[GPIOLampRood,0]]
lamp_lst = [GPIOLampGroen,GPIOLampOranje,GPIOLampRood]


# status = 0 -- Lamp uit, status = 1 -- Lamp Aan
#GPIO: int, status: zie boven, #knipper_interval: int, 0 = false
def lamp(GPIOLamp,status):
    #try:
        if status == 0:
            GPIO.output(GPIOLamp,GPIO.LOW)
            setLampStatus(GPIOLamp,0)
            return
        elif status == 1:
            GPIO.output(GPIOLamp,GPIO.HIGH)
            setLampStatus(GPIOLamp,1)
            return

def knipperLamp(id,tijd_interval):
    pass

def setLampStatus(lamp_id, status):
    global lamp_status
    for lampen in lamp_status:
        if lampen[0] == lamp_id:
            lampen[1] = status
            return True
    return False

def getLampStatus(lamp_id):
    global lamp_status
    for lampen in lamp_status:
        if lampen[0] == lamp_id:
            return lampen[1]

def isButtonPressed(id):
    input_state = GPIO.input(id)
    if input_state == False:
        print('Button {} Pressed'.format(id))
        return True
    return False

#Test scripts

while True:
    if isButtonPressed(GPIOKnop1):
        lamp(GPIOLampGroen,1)
        knipperLamp(GPIOLampOranje,0.5)
