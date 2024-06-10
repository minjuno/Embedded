import RPi.GPIO as GPIO
import adafruit_dht
import serial
import time

arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=None)

def read_arduino_data():
    line = arduino.readline()
    arr = line.split()
    data_type = arr[0]
    temperature = float(arr[1])
    humidity = float(arr[4])
    return data_type, temperature, humidity
   
def toggle_led():
    arduino.write(b'TOGGLE\n')
    time.sleep(0.08)

def toggle_gas():
    arduino.write(b'TOGGLE1\n')
    time.sleep(0.08)
