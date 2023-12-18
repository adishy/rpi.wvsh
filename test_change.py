from machine import Pin
import utime

# Assuming the switch is connected to GPIO 15, replace with your GPIO pin number
switch_pin = Pin(15, Pin.IN, Pin.PULL_DOWN)


if __name__ == '__main__':
    print("Hello there")
    a = 0
    while a <= 10:
        if switch_pin.value() == 1:  # Check if the switch is on (assuming active high)
            print(a, "Switch is ON")
        else:
            print(a, "Switch is OFF")
        a+=1 
        utime.sleep(0.5)  # Add a small delay to avoid flooding the serial output
