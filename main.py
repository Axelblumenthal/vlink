import display
import button
import led
import time
import os

path  = "data//"
dir_list = os.listdir(path)



print("VLINK Version 0.2")

print(dir_list)

while True:
    
    IP, Temp, RSSI ,SSID= display.get_info(False)
    #display.infopage(IP,Temp,RSSI)
    display.mainpage(str(RSSI,'utf-8')[:2])
    print(SSID)
    
    #display.get_info(False) # print debug data on screen
    button.get_input() #test buttons
    time.sleep(2)
    


