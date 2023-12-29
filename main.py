import display
import button
import led
import time
import os


path  = "data//"
dir_list = os.listdir(path)



print("VLINK Version 0.2")

print(dir_list)

try:
    # Start the thread
    button.button_1_thread.start()
    button.button_2_thread.start()
    button.button_3_thread.start()
    button.button_4_thread.start()

    # Main program loop
    while True:
        # Your main program logic can be executed here
        IP, Temp, RSSI ,SSID= display.get_info(False)
        #display.mainpage(str(RSSI,'utf-8')[:2],str(SSID,'utf-8'))
        if button.button_1_handler == True:
            display.infopage()
        else:
            display.mainpage(str(RSSI,'utf-8')[:2],str(SSID,'utf-8'))
        time.sleep(1)

except KeyboardInterrupt:
    # Cleanup GPIO settings
    button.io_cleanup()
    # Exit the program
    raise SystemExit

    


