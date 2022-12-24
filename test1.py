from machine import UART, Pin
import time
led_6 = Pin(6, Pin.OUT)
led_7 = Pin(7, Pin.OUT)
led_8 = Pin(8, Pin.OUT)
led_9 = Pin(9, Pin.OUT)
led_10 = Pin(10, Pin.OUT)
led_11 = Pin(11, Pin.OUT)
led_12 = Pin(12, Pin.OUT)
led_13 = Pin(13, Pin.OUT)
led_14 = Pin(14, Pin.OUT)
led_15 = Pin(15, Pin.OUT)
led_6.value(0)
led_7.value(0)
led_8.value(0)
led_9.value(0)
led_10.value(1)
led_11.value(0)
led_12.value(0)
led_13.value(1)
led_14.value(0)
led_15.value(0)

uart = UART(0, baudrate= 921600, tx=Pin(0), rx=Pin(1))  # init with given baudrate
uart.init(921600, bits=8, parity=None, stop=1)          # init with given parameters
print('-- UART Serial Test --')
print('>', end='')
txData = b'\r'
uart.write(txData.decode("ascii"))
time.sleep(1)

rxData = bytes()
while 1:
    txData = b'sample \r'
    uart.write(txData.decode("ascii"))
    rxData = uart.readline()
    line = rxData.decode("ascii")
    print(rxData)
    
    rxData = uart.readline()
    line = rxData.decode("ascii")
    print(rxData)
    time.sleep(0.3)
    if "MAX" in line:
        led_6.value(0)
        led_7.value(1)
        led_8.value(0)
        led_9.value(0)
        led_10.value(1)
        led_11.value(1)
        led_12.value(0)
        led_13.value(1)
        led_14.value(0)
        led_15.value(1)
        time.sleep(0.7)
        led_6.value(1)
        led_7.value(0)
        led_8.value(1)
        led_9.value(1)
        led_10.value(1)
        led_11.value(0)
        led_12.value(1)
        led_13.value(1)
        led_14.value(1)
        led_15.value(0)
        
    else:
        led_6.value(0)
        led_7.value(0)
        led_8.value(0)
        led_9.value(0)
        led_14.value(0)
        led_15.value(0)
        led_11.value(0)
        led_12.value(0)
        led_10.value(1)
        time.sleep(0.3)
        led_13.value(0)
        time.sleep(0.3)
        led_13.value(1)
        time.sleep(0.3)
        led_13.value(0)
        time.sleep(0.3)
        led_13.value(1)
        time.sleep(0.3)
        led_13.value(0)
        time.sleep(0.3)
        led_13.value(1)        
        time.sleep(0.5)
    time.sleep(2)
