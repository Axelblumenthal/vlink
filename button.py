import RPi.GPIO as GPIO
import threading

global button_left 
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

def io_cleanup():
    GPIO.cleanup()

def button_1_handler():
    LONG_PRESS_DURATION =2
    SHORT_PRESS_DURATION=0.5
    while True:
        
        input_state = GPIO.input(button_left)
        if input_state == False:  # Button pressed
            button_left = time.time()  # Record the press time

            # Wait for button release or long press
            while GPIO.input(button_left) == False:
                time.sleep(0.1)
                elapsed_time = time.time() - button_left

                if elapsed_time >= LONG_PRESS_DURATION:
                    print(f"Button left  long pressed")
                    # Perform action for a long press
                    break

            if elapsed_time < LONG_PRESS_DURATION:
                if elapsed_time < SHORT_PRESS_DURATION:
                    print(f"Button left  short pressed")
                    # Perform action for a short press
                else:
                    print(f"Button left pressed")
                    # Perform action for a normal press

            time.sleep(0.1)  # Delay to debounce

button_1_thread = threading.Thread(target=button_1_handler)


def get_input():
    page = 0 

        
        
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


    