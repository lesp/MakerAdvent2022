## Day 10 - Banana Pi Pico W

All of the code and images are in their respective folder.

The Bill of Materials is as follows
* [Banana Pi Pico W](https://www.aliexpress.com/item/1005004775634442.html)
* Dollar Store / Pound Shop LEDs (Battery Operated)
* NPN Transistor (2N 2222)
* Breadboard
* Wires
* Screw terminal
* 1K Ohm Resistor
* 10 Ohm Resistor

I [bought the Banana Pi Pico W from Aliexpress](https://www.aliexpress.com/item/1005004775634442.html) for around £10.

It came with CircuitPython pre-loaded, but it would be best practice to [flash the latest version.](https://circuitpython.org/board/bpi_picow_s3/)

The [HTTP server is Ampule](https://github.com/deckerego/ampule) by [John Ellis (deckerego)](https://github.com/deckerego) and it is excellent!

Node-RED was used to create a simple interface to control the LEDs. [More details on the Node-RED website.](https://nodered.org/)

The GUI creation tool for Python was [EasyGUI](https://easygui.readthedocs.io/en/latest/tutorial.html) which can be installed via pip.