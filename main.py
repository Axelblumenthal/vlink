import display
import button
import led
import time




print("VLINK Version 0.2")



while True:
    #display.mainpage()
    info = display.get_info

    display.infopage(info[1],info[2],info[3])
    
    display.get_info(False) # print debug data on screen
    button.get_input() #test buttons


