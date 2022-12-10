import board
import wifi
import socketpool
import ampule
import time
from digitalio import DigitalInOut, Direction

led = DigitalInOut(board.GP15)
led.direction = Direction.OUTPUT
led.value = False

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Access-Control-Allow-Origin": '*',
    "Access-Control-Allow-Methods": 'GET, POST',
    "Access-Control-Allow-Headers": 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
}

@ampule.route("/on")
def light_on(request):
    led.value = True
    return (200, headers, '{"Lights": on}')

@ampule.route("/off")
def light_off(request):
    led.value = False
    return (200, headers, '{"Lights": off}')

@ampule.route("/flash")
def flash(request):
    for i in range(10):
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)
    return (200, headers, '{"Lights": flash}')

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets not found in secrets.py")
    raise

try:
    print("Connecting to %s..." % secrets["ssid"])
    print("MAC: ", [hex(i) for i in wifi.radio.mac_address])
    wifi.radio.connect(secrets["ssid"], secrets["password"])
except:
    print("Error connecting to WiFi")
    raise

pool = socketpool.SocketPool(wifi.radio)
socket = pool.socket()
socket.bind(['0.0.0.0', 80])
socket.listen(1)
print("Connected to %s, IPv4 Addr: " % secrets["ssid"], wifi.radio.ipv4_address)

while True:
    ampule.listen(socket)