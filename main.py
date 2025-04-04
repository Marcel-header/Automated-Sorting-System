import cv2
import time
from proximity_sensor import object_detected
from color_detection import detect_color
from robotic_arm_control import move_arm

sorted_counts = {'red': 0, 'green': 0, 'blue': 0, 'unknown': 0}

cap = cv2.VideoCapture(0)

try:
    while True:
        if object_detected():
            ret, frame = cap.read()
            if not ret:
                print("Camera error: Frame not captured.")
                continue

            color = detect_color(frame)
            print(f"Detected color: {color}")

            if color in ['red', 'green', 'blue']:
                move_arm(color)
                sorted_counts[color] += 1
                print(f"Item placed in {color} tray. Total: {sorted_counts[color]}")
            else:
                sorted_counts['unknown'] += 1
                print("Error: Color could not be classified.")

            time.sleep(1)
            move_arm('home')

except KeyboardInterrupt:
    print("\nSorting stopped by user.")
    print("Final sorting counts:")
    for color, count in sorted_counts.items():
        print(f"{color.capitalize()}: {count}")
    cap.release()
