import serial
import cv2
import torch
from ultralytics import YOLO
import time
import random
import numpy as np

# Initialize YOLOv8 model
model = YOLO('yolov8n.pt')

# Initialize serial communication with Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Initialize camera
cap = cv2.VideoCapture(0)

# Robot states
STATE_MOVE = "MOVE"
STATE_COLLECT = "COLLECT"
STATE_REVERSE = "REVERSE" 
STATE_TURN = "TURN"
STATE_AVOID = "AVOID"
STATE_CHARGE = "CHARGE"

# Constants
COLLECTION_TIME = 5
REVERSE_TIME = 2
TURN_TIME = 3
TURN_ANGLE = 45
OBSTACLE_DISTANCE = 50  # cm
LOW_BATTERY_THRESHOLD = 20  # percent
CRITICAL_BATTERY_THRESHOLD = 10  # percent

# Global variables
robot_state = STATE_MOVE 
start_time = time.time()
battery_level = 100  # percent
total_trash_collected = 0
last_turn_direction = "LEFT"

def detect_objects(frame):
    results = model(frame)
    detected_objects = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detected_objects.append({
                'class': cls,
                'confidence': conf,
                'bbox': (x1, y1, x2, y2)
            })
    return detected_objects

def get_distance():
    # Simulated distance measurement with some noise
    base_distance = random.randint(10, 200)
    noise = random.uniform(-5, 5)
    return max(0, base_distance + noise)

def get_battery_level():
    global battery_level
    battery_drain = random.uniform(0.05, 0.15)  # Randomize battery drain
    battery_level -= battery_drain
    return max(0, battery_level)

def process_detections(detected_objects, current_state):
    global start_time, last_turn_direction, total_trash_collected

    battery = get_battery_level()
    if battery < CRITICAL_BATTERY_THRESHOLD:
        print("CRITICAL BATTERY! Returning to charging station.")
        return STATE_CHARGE
    elif battery < LOW_BATTERY_THRESHOLD and current_state != STATE_COLLECT:
        print("Low battery. Heading to charging station.")
        return STATE_CHARGE

    distance = get_distance()
    if distance < OBSTACLE_DISTANCE and current_state not in [STATE_REVERSE, STATE_TURN, STATE_AVOID]:
        print(f"Obstacle detected at {distance}cm. Avoiding.")
        return STATE_AVOID

    if current_state == STATE_COLLECT:
        if time.time() - start_time < COLLECTION_TIME:
            return STATE_COLLECT
        else:
            total_trash_collected += 1
            print(f"Finished collecting. Total trash collected: {total_trash_collected}")
    elif current_state == STATE_REVERSE:
        if time.time() - start_time < REVERSE_TIME:
            return STATE_REVERSE
        else:
            last_turn_direction = "RIGHT" if last_turn_direction == "LEFT" else "LEFT"
            return STATE_TURN
    elif current_state == STATE_TURN:
        if time.time() - start_time < TURN_TIME:
            return STATE_TURN
    elif current_state == STATE_AVOID:
        if time.time() - start_time < REVERSE_TIME:
            return STATE_AVOID
        else:
            return STATE_TURN

    # Trash detection
    trash_objects = [obj for obj in detected_objects if obj['class'] == 0 and obj['confidence'] > 0.6]
    if trash_objects:
        nearest_trash = max(trash_objects, key=lambda x: (x['bbox'][2] - x['bbox'][0]) * (x['bbox'][3] - x['bbox'][1]))
        print(f"Trash detected with confidence {nearest_trash['confidence']:.2f}. Collecting.")
        return STATE_COLLECT

    return STATE_MOVE

def send_command_to_arduino(command):
    global last_turn_direction
    if command == STATE_TURN:
        full_command = f"{command}_{last_turn_direction}"
    else:
        full_command = command
    arduino.write(full_command.encode())
    print(f"Sending command: {full_command}")

def draw_on_frame(frame, state, battery, detected_objects):
    cv2.putText(frame, f"State: {state}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, f"Battery: {battery:.1f}%", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, f"Trash Collected: {total_trash_collected}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    for obj in detected_objects:
        x1, y1, x2, y2 = obj['bbox']
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, f"Class: {obj['class']}, Conf: {obj['confidence']:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    return frame

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detected_objects = detect_objects(frame)
    new_state = process_detections(detected_objects, robot_state)
    
    if new_state != robot_state:
        print(f"State change: {robot_state} -> {new_state}")
        robot_state = new_state
        start_time = time.time()

    send_command_to_arduino(robot_state)

    battery = get_battery_level()
    frame = draw_on_frame(frame, robot_state, battery, detected_objects)
    cv2.imshow('River Cleaning Robot View', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
