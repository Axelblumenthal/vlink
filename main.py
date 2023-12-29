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
page =1
try:
    # Start the thread
    button.button_1_thread.start()
    button.button_2_thread.start()
    button.button_3_thread.start()
    button.button_4_thread.start()

    # Main program loop
    while True:
        if button.button_left_pressed == True:
            page += 1
        if button.button_right_pressed == True:
            page -= 1
        if page >= 2:
            page = 2
        if page <= 0:
            page = 0

        IP, Temp, RSSI ,SSID,CPU= display.get_info(False)

        if page == 1:
            display.mainpage(str(RSSI,'utf-8')[:2],str(SSID,'utf-8'))
        if page == 2:
            display.infopage(IP,Temp,RSSI,CPU)
        if page == 0:
            display.setting()
            

        #print(page)
        #display.mainpage(str(RSSI,'utf-8')[:2],str(SSID,'utf-8'))
        
          
        time.sleep(0.1)

except KeyboardInterrupt:
    # Cleanup GPIO settings
    #button.io_cleanup()
    # Exit the program
    raise SystemExit

    


