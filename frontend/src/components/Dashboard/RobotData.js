import React from 'react';

const RobotData = ({ data }) => {
  return (
    <div>
      <p>Location: {data.location}</p>
      <p>Path: {data.path}</p>
      <p>Accelerometer Data: {data.accelerometer}</p>
      <p>Battery Health: {data.battery}</p>
      <p>Safety Status: {data.safety}</p>
      <p>Time: {data.time}</p>
    </div>
  );
};

export default RobotData;
