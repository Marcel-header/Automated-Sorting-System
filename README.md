# Automated Object Sorting System using Mechatronics

This repository presents a simulation and prototype implementation of an automated object sorting system, designed as part of **Intel® Unnati Industrial Training 2025**.

- **Candidate:** Marcel Basumatary  
- **Mentor:** Assistant Professor Tandrali Ray  
- **Simulation Tool:** CoppeliaSim  
- **Microcontroller:** Raspberry Pi

---

## 🧠 Project Description

The system uses a combination of sensors and actuators to sort objects placed on a conveyor belt based on their color. It simulates a real-world mechatronics-based sorting mechanism using Raspberry Pi.

### 🛠️ How it works:

1. **Conveyor Belt Movement:** Objects of various colors (red, green, blue) move on a conveyor belt toward a sorting station.
2. **Color Detection:** A camera module identifies the object's color using computer vision (OpenCV).
3. **Position Sensing:** A proximity sensor detects when the object reaches the pick-up area.
4. **Robotic Arm Activation:** Once the object is in position, a robotic arm (controlled by six servo motors) is instructed to place the object into the correct color-coded bin.
5. **Sorting Completed:** The system resets to handle the next object.

---

## 📦 Components Used

| Hardware              | Role                                 |
|----------------------|--------------------------------------|
| Raspberry Pi         | Control logic and integration        |
| USB Camera           | Color detection                      |
| Proximity Sensor     | Detects object at pickup zone        |
| 6x Servo Motors      | Robotic arm actuation                |
| Conveyor Belt        | Object transportation                |
| Sorting Bins         | Red, Green, and Blue trays           |

---

## 📂 Repository Structure

```bash
├── code/
│   ├── color_detection.py
│   ├── proximity_sensor.py
│   ├── robotic_arm_control.py
│   └── main.py
├── docs/
│   └── Project_Report.pdf
├── media/
│   └── demo_video.mp4
└── README.md









