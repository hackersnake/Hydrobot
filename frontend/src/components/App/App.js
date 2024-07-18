import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import Navbar from '../Navbar/Navbar';
import RobotData from '../Dashboard/RobotData';
import CameraFeed from '../Dashboard/CameraFeed';
import RobotPathMap from '../Dashboard/RobotPathMap';
import RobotControls from '../Dashboard/RobotControls';
import Footer from '../Footer/Footer';
import config from './config';
import './App.css';

const socket = io(config.backendUrl);

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch(`${config.backendUrl}/robot_data`)
      .then(response => response.json())
      .then(data => setData(data));

    socket.on('update_data', (newData) => {
      setData(newData);
    });

    return () => {
      socket.off('update_data');
    };
  }, []);

  const sendCommand = (command) => {
    fetch(`${config.backendUrl}/set_robot_ip`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(command),
    });
  };

  return (
    <div className="App">
      <Navbar />
      <div className="container mt-3">
        <RobotData data={data} />
        <CameraFeed />
        <RobotPathMap path={data.path} />
        <RobotControls sendCommand={sendCommand} />
      </div>
      <Footer />
    </div>
  );
}

export default App;
