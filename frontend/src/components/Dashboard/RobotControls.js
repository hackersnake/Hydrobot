import React from 'react';

const RobotControls = ({ sendCommand }) => {
  const handleCommand = (command) => {
    sendCommand(command);
  };

  return (
    <div>
      <button onClick={() => handleCommand('reset')}>Reset</button>
      <button onClick={() => handleCommand('returnToBase')}>Return to Base</button>
    </div>
  );
};

export default RobotControls;
