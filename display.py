from luma.core.interface.serial import i2c
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1327
from PIL import ImageFont
import time 
from datetime import datetime
import subprocess



#Display Einrichten
serial = i2c(port=1,address=0x3D)
device = ssd1327(serial)

#

#font_path = "/home/blume/Video_Link/Video_Link/arial.ttf"

############################### Anzeigefunktionen und Symbole ######################################

def get_info(print_debug):

    RSS_Int=0
    cmd = "top -bn1 | grep load | awk '{printf \"CPU: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    Temp = subprocess.check_output(cmd, shell = True )
    cmd = "iwconfig wlan0 | grep Quality | cut -d '=' -f2"
    RSSI = subprocess.check_output(cmd, shell = True )
    cmd = "iwconfig wlan0 | grep ESSID | cut -d ':' -f2"
    SSID = subprocess.check_output(cmd, shell = True )
    cmd = "iwconfig wlan0 | grep Signal level "
    Signallevel = subprocess.check_output(cmd, shell = True )
    
    if str(RSSI,'utf-8')[:2] == '':
        RSSI = 0
    else:
       RSS_Int= str(RSSI,'utf-8')[:2]
    
    if print_debug == True:
        print(str(Signallevel,'utf-8')+"RSSI: "+str(RSSI)+ "    IP: " + str(IP,'utf-8') + " Temp: "+str(Temp,'utf-8') +str(CPU,'utf-8'))
    

    return IP,Temp,RSS_Int,SSID,CPU

# Zeigt akuell verbundene Ger te an
def devices(draw):
   # font_size = 15
   # font = ImageFont.truetype(font_path,font_size)
    draw.text((10,60),"no device !",fill="white")

def print_SSSID(draw,SSID):
    #font_size = 15
    #font = ImageFont.truetype(font_path,font_size)
    draw.text((10,80),SSID,fill="white")
    


# Zeigt aktuelle Uhrzeit an
def time(draw):
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M")
   # font_size = 15
    #font_path = "data//ARCADECLASSIC.TTF"
    #arial_font = ImageFont.load_default(         )
    #font = ImageFont.truetype(font_path,font_size)
    draw.text((10,40),currentTime,fill="white")
    

def network_rssi(draw,percent):
    x_offset = 102
    if int(percent) > 60:
        draw.rectangle((22+x_offset,1,24+x_offset,15), outline="white",fill="white") ###############
        draw.rectangle((17+x_offset,3,19+x_offset,15), outline="white",fill="white") #############
        draw.rectangle((12+x_offset,6,14+x_offset,15), outline="white",fill="white") ###########
        draw.rectangle((7+x_offset,9,9+x_offset,15), outline="white",fill="white") #########
        draw.rectangle((2+x_offset,13,4+x_offset,15), outline="white",fill="white") ######
    if int(percent)  > 50:
        
        draw.rectangle((17+x_offset,3,19+x_offset,15), outline="white",fill="white") #############
        draw.rectangle((12+x_offset,6,14+x_offset,15), outline="white",fill="white") ###########
        draw.rectangle((7+x_offset,9,9+x_offset,15), outline="white",fill="white") #########
        draw.rectangle((2+x_offset,13,4+x_offset,15), outline="white",fill="white") ######

    if int(percent)  > 40:
        
        draw.rectangle((12+x_offset,6,14+x_offset,15), outline="white",fill="white") ###########
        draw.rectangle((7+x_offset,9,9+x_offset,15), outline="white",fill="white") #########
        draw.rectangle((2+x_offset,13,4+x_offset,15), outline="white",fill="white") ######7

    if int(percent)  > 30: 
        draw.rectangle((7+x_offset,9,9+x_offset,15), outline="white",fill="white") #########
        draw.rectangle((2+x_offset,13,4+x_offset,15), outline="white",fill="white") ######

    if int(percent)  > 20:
        draw.rectangle((2+x_offset,13,4+x_offset,15), outline="white",fill="white") ######
        
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
    

def menue_sidebar(draw):
    bar_height = 12
    #font_size = 12
    #font = ImageFont.truetype("/home/blume/Video_Link/Video_Link/arial.ttf",font_size)
    
    draw.rectangle((0,127- bar_height,42,127),outline ="white",fill=None)
    draw.text((2,128 - bar_height),"INFO",fill="white")

    draw.rectangle((42,127 - bar_height,84,127),outline ="white",fill=None)
    draw.text((43 ,128 - bar_height),"HOME",fill="white")

    draw.rectangle((84,127 - bar_height,127,127),outline ="white",fill=None)
    draw.text((85,128 - bar_height),"SETTINGS",fill="white")

############################## Bildschirme und Men f hrung ###################################



def mainpage(RSSI,SSID):
    #print("Mainpage")
    with canvas(device) as draw:
        time(draw) # Zeit 
        battery(draw,95) # Batterie oben rechts 
        devices(draw) 
        print_SSSID(draw,SSID)
        network_rssi(draw,RSSI)
        menue_sidebar(draw)
     
def infopage(IP,Temp,RSSI,CPU):
    
    with canvas(device) as draw:
        draw.text((5, 5), "IP: " + str(IP,'utf-8'), fill=255)
        draw.text((5,15),"Temp: "+str(Temp,'utf-8'), fill=255)
    #    rssi_short = int(str(RSSI,'utf-8')[:2])
        draw.text((5,25),"RSSI: "+str(RSSI), fill=255)
        draw.text((5,35),str(CPU,'utf-8'), fill=255)
        
    

def setting():
   # print("Settings")
    menue_number = 1
    
    with canvas(device) as draw:
        menue_rect(draw,menue_number)
        
    return 0

def user_interface():
    
    user_comando = 1
    return user_comando
    
    
