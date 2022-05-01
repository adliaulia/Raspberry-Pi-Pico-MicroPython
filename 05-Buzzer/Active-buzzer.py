from machine import Pin
from time import sleep

buzz = Pin(6, Pin.OUT)

while True:
    buzz.value(1)
    sleep(1)
    buzz.value(0)
    sleep(1)