import RPi.GPIO as GPIO

button_left = 12 #Button Left
button_right = 21 # Button Right
button_up    = 20 # Button UP
button_down = 16 # Button Down

import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(button_left, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_right, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)




def get_input():
    page = 0 
    while( GPIO.input(button_left) == GPIO.HIGH):
        print("Button left")
        page = page +1
        time.sleep(0.2)
        #mainpage()
        
        
    while( GPIO.input(button_right) == GPIO.HIGH):
        print("Button right")
        page = page -1
        time.sleep(0.2),
       # infopage()
               
    while( GPIO.input(button_up) == GPIO.HIGH):
        print("Button up")
        page = page -1
        time.sleep(0.2),
       # infopage()
               
    while( GPIO.input(button_down) == GPIO.HIGH):
        print("Button down")
        page = page -1
        time.sleep(0.2),
       # infopage()
    