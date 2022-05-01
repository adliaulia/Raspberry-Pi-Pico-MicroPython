from machine import Pin
import time

LED = Pin(25, Pin.OUT)

while True:
    LED.toggle()
    time.sleep(0.5)