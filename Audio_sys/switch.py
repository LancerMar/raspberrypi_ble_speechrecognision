import RPi.GPIO as GPIO
import time


Switch_input_pin = 29

GPIO.setmode(GPIO.BOARD)

GPIO.setup(Switch_input_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def switch(channel):
    if(GPIO.input(channel)):
        print("loose the switch")
    else:
        print("press the switch")


# callback function
GPIO.add_event_detect(Switch_input_pin,GPIO.BOTH,callback=switch,bouncetime=200)

while(True):
    print("processing...")
    time.sleep(1)
    pass