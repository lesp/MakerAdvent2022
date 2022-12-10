import requests
import time
import easygui as eg
import sys
for i in range(10):
    requests.get("http://192.168.0.7/on")
    time.sleep(0.2)
    requests.get("http://192.168.0.7/off")
    time.sleep(0.2)

try:
    while True:
        controls = eg.buttonbox(title="LED Controls", msg="Control the LEDs!", choices=["On","Off"])
        print(controls)
        if controls == "On":
            requests.get("http://192.168.0.7/on")
        elif controls == "Off":
            requests.get("http://192.168.0.7/off")
        time.sleep(1)
except KeyboardInterrupt:
    print("Error")
    sys.exit()
    
