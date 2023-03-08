import React, { useEffect, useState } from "react";

const LoadAPI = ({ url }) => {
  const [hid, setHid] = useState({});

  useEffect(() => {
    const fetchData = () => {
      return fetch(url)
        .then((res) => res.json())
        .then((data) => setHid(data));
    };
    fetchData();
  }, [url]);
  return (
    <div>
      {hid && (
        <h2>
          <pre>{JSON.stringify(hid, null, 2)}</pre>
        </h2>
      )}
    </div>
  );
};

export default LoadAPI;
