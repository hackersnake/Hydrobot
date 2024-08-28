import React, { useState } from 'react';

const Navbar = ({ setRobotIP }) => {
  const [robotIP, setIP] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    setRobotIP(robotIP);
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <a className="navbar-brand" href="#">Hydrobot</a>
      <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav ml-auto">
          <li className="nav-item">
            <form className="form-inline" onSubmit={handleSubmit}>
              <input className="form-control mr-sm-2" type="text" placeholder="Robot IP" value={robotIP} onChange={(e) => setIP(e.target.value)} />
              <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Set IP</button>
            </form>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
