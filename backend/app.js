const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: "http://localhost:9801",
    methods: ["GET", "POST"]
  }
});

app.use(cors());
app.use(express.json());

let robotIp = '';

app.post('/set_robot_ip', (req, res) => {
  robotIp = req.body.robot_ip;
  res.send({ success: true, robotIp });
});

app.get('/robot_data', (req, res) => {
  const data = {
    location: "12.9716, 77.5946",
    path: "Path data",
    accelerometer: "Accelerometer data",
    battery: "Battery health data",
    safety: "Safety status",
    time: new Date().toLocaleString()
  };
  res.json(data);
});

io.on('connection', (socket) => {
  console.log('New client connected');
  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});

const PORT = 9802;
server.listen(PORT, () => console.log(`Backend server running on port ${PORT}`));
