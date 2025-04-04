import RPi.GPIO as GPIO
import time

PROXIMITY_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PROXIMITY_PIN, GPIO.IN)

def object_detected():
    return GPIO.input(PROXIMITY_PIN) == GPIO.HIGH
