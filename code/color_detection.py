import cv2
import numpy as np

def detect_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red_mask = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))
    green_mask = cv2.inRange(hsv, (40, 70, 70), (80, 255, 255))
    blue_mask = cv2.inRange(hsv, (100, 150, 0), (140, 255, 255))

    if red_mask.sum() > green_mask.sum() and red_mask.sum() > blue_mask.sum():
        return 'red'
    elif green_mask.sum() > red_mask.sum() and green_mask.sum() > blue_mask.sum():
        return 'green'
    elif blue_mask.sum() > red_mask.sum() and blue_mask.sum() > green_mask.sum():
        return 'blue'
    else:
        return 'unknown'
