from luma.core.interface.serial import i2c
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1327
from PIL import ImageFont


import subprocess
import os



import asyncio
import threading


#Display Einrichten
serial = i2c(port=1,address=0x3D)
device = ssd1327(serial)

#

font_path = "/home/blume/Video_Link/Video_Link/arial.ttf"

############################### Anzeigefunktionen und Symbole ######################################

def get_info(print_debug):
    
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    Temp = subprocess.check_output(cmd, shell = True )
    cmd = "iwconfig wlan0 | grep Quality | cut -d '=' -f2"
    RSSI = subprocess.check_output(cmd, shell = True )
    
    if print_debug == True:
        print("RSSI: "+str(RSSI,'utf-8')[:2] + "    IP: " + str(IP,'utf-8') + " Temp: "+str(Temp,'utf-8') )
    time.sleep(2)
    return IP,Temp,RSSI

# Zeigt akuell verbundene Ger te an
def devices(draw):
    font_size = 15
    font = ImageFont.truetype(font_path,font_size)
    draw.text((10,60),"no device !",font = font,fill="white")
    


# Zeigt aktuelle Uhrzeit an
def time(draw):
    font_size = 15
    #arial_font = ImageFont.load_default(         )
    font = ImageFont.truetype(font_path,font_size)
    draw.text((10,40),"13:50",font = font,fill="white")
    

def network_rssi(draw,percent):
    if percent > 60:
        draw.rectangle((22,1,24,15), outline="white",fill="white") ###############
        draw.rectangle((17,3,19,15), outline="white",fill="white") #############
        draw.rectangle((12,6,14,15), outline="white",fill="white") ###########
        draw.rectangle((7,9,9,15), outline="white",fill="white") #########
        draw.rectangle((2,13,4,15), outline="white",fill="white") ######
        
    return 0

# Zeigt Battery symbol an mit 3 balken an 
def battery(draw,percent): #TODO Bei unter 20% Blinken
    draw.rectangle((2,2,40,15), outline="white",fill="black")
    draw.rectangle((40,3,42,13), outline="white",fill="black")
    
    if percent > 80:
        
        draw.rectangle((29,4,38,13), outline="white",fill="white")
        draw.rectangle((16,4,26,13), outline="white",fill="white")
        draw.rectangle((4,4,13,13), outline="white",fill="white")
           
    if percent <= 60 and percent >= 41:
        
        draw.rectangle((16,4,26,13), outline="white",fill="white")
        draw.rectangle((4,4,13,13), outline="white",fill="white")
            
    if percent <= 40 and percent >= 20:
        print("Low Battery !")
        draw.rectangle((4,4,13,13), outline="white",fill="white")    
        
# Zeigt ein rechteck als men f hrung an,         
def menue_rect(draw,number): 
    draw.rectangle((0,32*number,128,32+(32*number)),outline="white", fill=None)
    return 0
    
            
############################## Bildschirme und Men f hrung ###################################
def mainpage():
    #print("Mainpage")
    with canvas(device) as draw:
        time(draw) # Zeit 
        battery(draw,95) # Batterie oben rechts 
        devices(draw) 
        # Netzqualtit t
     
def infopage():
    
    with canvas(device) as draw:
        draw.text((5, 5), "IP: " + str(IP,'utf-8'), fill=255)
        draw.text((5,15),"Temp: "+str(Temp,'utf-8'), fill=255)
        rssi_short = int(str(RSSI,'utf-8')[:2])
        draw.text((5,25),"RSSI: "+str(RSSI,'utf-8')[:6], fill=255)
        draw.text((5,35),"Page"+str(page),fill=255)
    

def setting():
   # print("Settings")
    #menue_number = 1
    
    #with canvas(device) as draw:
    #   menue_rect(draw,menue_number)
        
    return 0

def user_interface():
    
    user_comando = 1
    return user_comando
    
    
