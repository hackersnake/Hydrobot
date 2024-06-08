# Hyderobot

## Overview

Hyderobot is an ML and IoT-based robot designed to clean water bodies by collecting floating waste. Using a combination of sensors and cameras, it autonomously navigates through the water, detecting and pulling debris into a trash compartment. The robot sends live data to a server, allowing operators to monitor and control its operations remotely.

## Features

- **Live Camera Feed**: Displays continuous live footage from the robot's camera, allowing operators to monitor the water body.
- **Autonomous Navigation**: The robot uses an automatic navigation algorithm to travel through the water body.
- **Debris Collection**: Equipped with sensors and actuators, the robot detects and collects floating waste, storing it in a trash compartment.
- **Real-time Data Monitoring**: Operators can view live data including the robot's GPS location, accelerometer readings, battery health, and safety status.
- **Control Commands**: Operators can command the robot to return to its original location, reset, or perform other actions.
- **Connection Status**: Displays the connection status of the robot to ensure reliable communication.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure the Raspberry Pi IP address in `config.py`.

## Usage

1. Start the Flask server:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Use the dashboard to monitor the robot's data and send commands.

## Project Structure

```plaintext
.
├── app.py               # Main Flask application
├── config.py            # Configuration file containing IP addresses and URLs
├── requirements.txt     # Python dependencies
├── templates
│   └── index.html       # HTML file for the dashboard
├── static
│   ├── css
│   │   └── style.css    # Custom CSS styles
│   └── js
│       └── script.js    # JavaScript functionalities
└── README.md            # Project README file
