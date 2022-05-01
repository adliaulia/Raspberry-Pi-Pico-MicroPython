from machine import Pin, PWM
from time import sleep

buzzer = PWM(Pin(6))

tone = {
    "B0": 31,
    "C1": 33,
    "CS1": 35
    }

song = ["B0", "C1", "CS1"]

def playtone(frequency):
    buzzer.duty_u16(2000)
    buzzer.freq(frequency)
    
def bequiet():
    buzzer.duty_u16(0)

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
        else:
            playtone(tone[mysong[i]])
        sleep(0.3)
    bequiet()
    
while True:
    playsong(song)
    sleep(1)