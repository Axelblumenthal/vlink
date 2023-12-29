import display
import button
#from button import button_left_pressed
import led
import time
import os


path  = "data//"
dir_list = os.listdir(path)



print("VLINK Version 0.2")

print(dir_list)
page =0
try:
    # Start the thread
    button.button_1_thread.start()
    button.button_2_thread.start()
    button.button_3_thread.start()
    button.button_4_thread.start()

    # Main program loop
    while True:
        IP, Temp, RSSI ,SSID= display.get_info(False)

        if page == 0:
            display.mainpage(str(RSSI,'utf-8')[:2],str(SSID,'utf-8'))
        if page == 1:
            display.infopage(IP,Temp,RSSI)
        if page == 2:
            display.setting()
            

        print(page)
        #display.mainpage(str(RSSI,'utf-8')[:2],str(SSID,'utf-8'))
        if button.button_left_pressed == True and page <= 1:
            page += 1
          
        time.sleep(0.1)

except KeyboardInterrupt:
    # Cleanup GPIO settings
    #button.io_cleanup()
    # Exit the program
    raise SystemExit

    


