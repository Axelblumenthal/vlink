import cv2
import socket
import pickle
import os
from datetime import datetime
import subprocess
import time
import threading



# In order to iterate over a block of code as long as the test expression is true
def transmit():
    # AF_INET refers to the address of family of ip4v
# SOCK_DGRAM means connection-oriented UDP protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Gives UDP protocol to follow
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1900000)  # Set socket buffer size
    serverip = "192.168.178.45"  # Server public IP
    serverport = 2323  # Server Port Number to identify the process that needs to receive or send packets

# Set the desired resolution to 720p (1280x720)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

    qual = 85
    desired_bitrate_mbps = 40
    while True:
        start_time = time.time()

        cmd = "vcgencmd measure_temp | cut -f 2 -d '='"
        Temp = subprocess.check_output(cmd, shell=True)
        Temp = str(Temp, 'utf-8')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        cmd = "iwconfig wlan0 | grep Quality | cut -d '=' -f2"
        RSSI = subprocess.check_output(cmd, shell=True)
        RSSI = str(RSSI, 'utf-8')[:2]

        ret, photo = cap.read()  # Start Capturing images/video
        photo = cv2.putText(photo, 'Time: ' + current_time + '    Temp:' + Temp + '   RSSI:' + RSSI,
                        (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        ret, buffer = cv2.imencode(".jpg", photo, [int(cv2.IMWRITE_JPEG_QUALITY), qual])
        x_as_bytes = pickle.dumps(buffer)

        s.sendto(x_as_bytes, (serverip, serverport))

        end_time = time.time()
        elapsed_time = end_time - start_time

    # Calculate the time to sleep to achieve the desired bitrate
        desired_bitrate_bps = desired_bitrate_mbps * 1e6
        frame_size_bits = len(x_as_bytes) * 8
        time_to_sleep = max(0, (frame_size_bits / desired_bitrate_bps) - elapsed_time)
        time.sleep(time_to_sleep)

        #if cv2.waitKey(10) == 13:  # Press Enter then window will close
            
transmit_thread = threading.Thread(target=transmit)
# Destroy all Windows/close
#cv2.destroyAllWindows()
#cap.release()

