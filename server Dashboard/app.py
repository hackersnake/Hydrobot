# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', robot_ip=config.ROBOT_IP, connected=is_robot_connected())

@app.route('/update_data', methods=['POST'])
def update_data():
    data = request.get_json()
    socketio.emit('update_data', data)
    return '', 204

@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.json.get('command')
    # Handle sending the command to the robot
    # e.g., send a request to the robot's API
    return '', 204

@app.route('/set_robot_ip', methods=['POST'])
def set_robot_ip():
    new_ip = request.form.get('robot_ip')
    config.ROBOT_IP = new_ip
    return redirect(url_for('index'))

def is_robot_connected():
    # Implement logic to check if the robot is connected
    # For demonstration, assume it is always connected
    return True

@socketio.on('connect')
def handle_connect():
    emit('status', {'connected': is_robot_connected()})

if __name__ == '__main__':
    socketio.run(app, host=config.FLASK_SERVER_IP, port=config.FLASK_SERVER_PORT, debug=True)
