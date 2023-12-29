import display
import button
import led
import time
import keyboard

def stop_program():
    print("Program stopped")
    exit(0)  # Exiting the program when 'Esc' or 'Ctrl + C' is pressed
    
# Listen for 'Esc' key or 'Ctrl + C' to stop the program
keyboard.add_hotkey('esc', stop_program)
keyboard.add_hotkey('ctrl+c', stop_program)

print("VLINK Version 0.2")


while True:
    display.mainpage()
    display.get_info(False) # print debug data on screen
    button.get_input() #test buttons
