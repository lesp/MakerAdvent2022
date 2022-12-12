import time

import adafruit_dht
import board

dht = adafruit_dht.DHT11(board.GP16)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as e:
        print("Reading from DHT failure: ", e.args)

    time.sleep(1)