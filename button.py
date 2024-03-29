import RPi.GPIO as GPIO
import threading

 
button_left = 12 #Button Left
button_right = 21 # Button Right
button_up    = 20 # Button UP
button_down = 16 # Button Down


button_left_pressed = False
button_right_pressed = False
button_up_pressed = False
button_down_pressed = False

import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(button_left, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_right, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def io_cleanup():
    GPIO.cleanup()



def button_1_handler():
    global button_left_pressed
    while True:
        input_state = GPIO.input(button_left)
        if input_state == True:
            print("Button left pressed")
            button_left_pressed = True
            # Do something when button 1 is pressed
        else:
            button_left_pressed = False
        time.sleep(0.1)
        
   

def button_2_handler():
    global button_right_pressed
    while True:
        input_state = GPIO.input(button_right)
        if input_state == True:
            print("Button right pressed")
            button_right_pressed = True
        else:
            button_right_pressed = False
            
            # Do something when button 1 is pressed
        time.sleep(0.1)
        

def button_3_handler():
    while True:
        global button_up_pressed
        input_state = GPIO.input(button_up)
        if input_state == True:
            print("Button up pressed")
            button_up_pressed = True
        else:
            button_up_pressed = False
            # Do something when button 1 is pressed
            time.sleep(0.5)
        

def button_4_handler():
    global button_down_pressed
    while True:
        input_state = GPIO.input(button_down)
        if input_state == True:
            print("Button down pressed")
            button_down_pressed = True
        else:
            button_down_pressed = False
            # Do something when button 1 is pressed
        time.sleep(0.5)


button_1_thread = threading.Thread(target=button_1_handler)
button_2_thread = threading.Thread(target=button_2_handler)
button_3_thread = threading.Thread(target=button_3_handler)
button_4_thread = threading.Thread(target=button_4_handler)




    