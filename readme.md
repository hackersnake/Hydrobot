# River Cleaning Robot with YOLOv8

## Overview

This project implements an autonomous river cleaning robot using computer vision (YOLOv8) for trash detection, and a Raspberry Pi + Arduino Uno setup for control. The robot navigates waterways, detects and collects trash, avoids obstacles, and manages its battery level.

## Features

- Real-time object detection using YOLOv8
- Autonomous navigation and trash collection
- Obstacle avoidance
- Battery level monitoring
- State-based robot control (Move, Collect, Avoid, Charge, etc.)
- Serial communication between Raspberry Pi and Arduino Uno

## Requirements

- Raspberry Pi (with camera module)
- Arduino Uno
- YOLOv8 model
- Python 3.7+
- OpenCV
- PyTorch
- Ultralytics YOLO
- pyserial

## Installation

1. Clone this repository:
2. Install the required Python packages:
3. Download the YOLOv8 model (or train your own for specific trash detection).

4. Connect your Raspberry Pi to the Arduino Uno via USB.

5. Set up your robot's hardware (motors, sensors, etc.) and connect to the Arduino.

## Usage

1. Upload the Arduino sketch (not included in this repo) to your Arduino Uno.

2. Run the main Python script on your Raspberry Pi:

3. The robot will start in the MOVE state and begin its cleaning operation.

## Code Structure

- `river_cleaning_robot.py`: Main Python script for the Raspberry Pi
- `arduino_control.ino`: Arduino sketch for motor and sensor control (not included)

## State Machine

The robot operates based on the following states:
- MOVE: Default movement
- COLLECT: Collecting detected trash
- REVERSE: Moving backwards (usually before turning)
- TURN: Changing direction
- AVOID: Avoiding detected obstacles
- CHARGE: Returning to charging station

## Customization

- Adjust the `COLLECTION_TIME`, `REVERSE_TIME`, `TURN_TIME`, and other constants in the code to fine-tune the robot's behavior.
- Modify the `detect_objects` function if using a custom-trained YOLO model.

## Contributing

Contributions to improve the robot's functionality are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- YOLOv8 by Ultralytics
- OpenCV community
- Arduino community
