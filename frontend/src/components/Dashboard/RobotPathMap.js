import React, { useEffect } from 'react';

const RobotPathMap = ({ pathCoordinates }) => {
  useEffect(() => {
    const map = new window.google.maps.Map(document.getElementById('robotPathMap'), {
      center: { lat: 0, lng: 0 },
      zoom: 10,
    });

    const path = new window.google.maps.Polyline({
      path: pathCoordinates,
      geodesic: true,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 2,
    });

    path.setMap(map);
  }, [pathCoordinates]);

  return <div id="robotPathMap" style={{ height: '300px', width: '100%' }}></div>;
};

export default RobotPathMap;
