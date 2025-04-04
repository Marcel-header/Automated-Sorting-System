from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

positions = {
    'home': [90, 90, 90, 90, 90, 90],
    'red': [45, 80, 100, 60, 90, 90],
    'green': [60, 70, 90, 65, 90, 90],
    'blue': [75, 60, 85, 70, 90, 90]
}

def move_arm(position):
    for i, angle in enumerate(positions[position]):
        kit.servo[i].angle = angle
        time.sleep(0.1)