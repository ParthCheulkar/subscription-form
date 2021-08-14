import logo from "./logo.svg";
import "./App.css";
import { useEffect, useState } from "react";

function App() {
  const [subs, setSubs] = useState();

  return (
    <div className="App">
      <h2 className="heading">
        Subscr<span className="dot">i</span>be to our Newsletter
      </h2>
      <span></span>
      <form>
        <input
          className="email"
          type="text"
          value={subs}
          onChange={(e) => setSubs(e.target.value)}
          placeholder="Enter email"
        ></input>
        <button
          className="button"
          type="submit"
          value="Subscribe"
          onClick={async (e) => {
            // const sub_ = { subs };
            e.preventDefault();
            const response = await fetch("http://127.0.0.1:5000/post", {
              method: "POST", // or 'PUT'
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({ subs: subs }),
            })
              .then((response) => {
                response.json();
                setSubs("");
              })
              .then((data) => {
                console.log("Success:", data);
              })
              .catch((error) => {
                console.error("Error:", error);
              });
          }}
        >
          Subscribe
        </button>
      </form>
    </div>
  );
}

export default App;
