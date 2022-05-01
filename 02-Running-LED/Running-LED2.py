from machine import Pin
from time import sleep

led0 = Pin(0, Pin.OUT)
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)
led4 = Pin(4, Pin.OUT)
led5 = Pin(5, Pin.OUT)

def led(no):
    if no == 0:
        led0.value(1)
        sleep(0.5)
        led0.value(0)
    elif no == 1:
        led1.value(1)
        sleep(0.5)
        led1.value(0)
    elif no == 2:
        led2.value(1)
        sleep(0.5)
        led2.value(0)
    elif no == 3:
        led3.value(1)
        sleep(0.5)
        led3.value(0)
    elif no == 4:
        led4.value(1)
        sleep(0.5)
        led4.value(0)
    elif no == 5:
        led5.value(1)
        sleep(0.5)
        led5.value(0)
        
while True:
    for x in range(6):
        led(x)