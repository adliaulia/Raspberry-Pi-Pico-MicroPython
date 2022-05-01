from machine import Pin, ADC
from time import sleep

analog_value = ADC(4)

while True:
    reading = analog_value.read_u16()
    vin = reading * 3.3 / 65535
    temperature = 27 - (vin - 0.706)/0.001721
    print('Input:', vin, '\nTemperature:', temperature)
    sleep(1)