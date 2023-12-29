import display
import button
import led
import time




print("VLINK Version 0.2")



while True:
    
    IP, Temp, RSSI = display.get_info(False)
    #display.infopage(IP,Temp,RSSI)
    display.mainpage(str(RSSI,'utf-8')[:6])
    
    #display.get_info(False) # print debug data on screen
    button.get_input() #test buttons
    time.sleep(2)
    


