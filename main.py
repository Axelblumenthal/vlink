import display
import button
#from button import button_left_pressed
import led
import time
import os
from datetime import datetime



# TODO Argumente beim start für debugging einbauen
# TODO Logging der Daten einbauen
# TODO Programm crach sicher machen ?
# TODO Menü einbauen , Netzwerkwechsel , stream start usw

# TODO GPS and Battery Suppor as well as 5 Button input


file_path = '/mnt/usb/example_file.txt'  # Path to the file you want to create

# Writing content to the file
with open(file_path, 'w') as file:
    file.write("This is some content written to the file.\n")
    file.write("You can add more lines as needed.\n")
    # Add any content you want inside the file

print(f"File '{file_path}' has been created.")




print("VLINK Version 0.2")




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
            display.mainpage(RSSI,str(SSID,'utf-8'))
        if page == 2:
            display.infopage(IP,Temp,RSSI,CPU)
        if page == 0:
            display.setting()
            

        #print(page)
        #display.mainpage(str(RSSI,'utf-8')[:2],str(SSID,'utf-8'))
        
          
        time.sleep(1)

except KeyboardInterrupt:
    # Cleanup GPIO settings
    #button.io_cleanup()
    # Exit the program
    raise SystemExit

    


