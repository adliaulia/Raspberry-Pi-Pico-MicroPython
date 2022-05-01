from machine import Pin
from time import sleep

btn1 = Pin(3, Pin.IN, Pin.PULL_UP)
btn2 = Pin(4, Pin.IN, Pin.PULL_UP)
btn3 = Pin(5, Pin.IN, Pin.PULL_UP)

led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)

while True:
    if btn1.value() == 0:
        led1.value(1)
    elif btn2.value() == 0:
        led2.value(1)
    elif btn3.value() == 0:
        led3.value(1)
    else:
        led1.value(0)
        led2.value(0)
        led3.value(0)
    sleep(0.02)