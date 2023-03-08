import { useState } from "react";
import LoadAPI from "../API/LoadAPI";
import "./App.css";

function App() {
  const [urlstr, setUrlstr] = useState("http://localhost/api/");
  const [tstr, setTstr] = useState("");
  const [rndKey, setRndKey] = useState(0);

  let handleChange = ({ target }) => {
    console.log(target);
    setTstr(target.value);
  };
  let handleChange2 = ({ target }) => {
    setRndKey(Math.random());
    setUrlstr(tstr);
    console.log(target, rndKey);
  };
  return (
    <>
      {/* <h1>Hello World</h1> */}
      <input
        type="text"
        defaultValue={urlstr}
        placeholder="http://localhost/api/"
        className="urltext"
        onChange={handleChange}
      />
      <button type="button" onClick={handleChange2} className="urlbutton">
        Fetch
      </button>
      <LoadAPI url={urlstr} rndKey={rndKey}></LoadAPI>
    </>
  );
}

export default App;
