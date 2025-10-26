// import { useState, useEffect } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'


import React from 'react'
import ReactDOM from 'react-dom/client'

// import MapView from './MapView.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <MapView />
  </React.StrictMode>
)

export default function App() {

  const [data] = useState(null);
  const [showPopup] = useState(false);

  // Fetch data from Flask
  const fetchData = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:5000/api/data");
      setData(res.data);
      setShowPopup(true); // show popup after fetching
    } catch (err) {
      console.error(err);
    }
  };

  const closePopup = () => setShowPopup(false);

  return (

    // popup stuff that we can delete later, for testing purposes
    <div>
          <div>
      <h1>Flask ↔ React Popup Demo</h1>
      <button onClick={fetchData}>Get Data from Flask</button>

      {showPopup && (
        <div style={popupOverlayStyle}>
          <div style={popupStyle}>
            <h2>Data from Flask</h2>
            <pre>{JSON.stringify(data, null, 2)}</pre>
            <button onClick={closePopup}>Close</button>
          </div>
        </div>
      )}
    </div>
    


      <h1>CheapBananas Map</h1>
      <MapView />
    </div>
  );
}


// function App() {
//   const [count, setCount] = useState(0)

//   const [data, setdata] = useState({
//         name: "",
//         age: 0,
//         date: "",
//         programming: "",
//     });

//   useEffect(() => {
//     // Fetch data from the Flask backend
//     fetch('/data')
//       .then(response => response.json())
//       .then(data => {
//         setdata({
//           name: data.Name,
//           age: data.Age,
//           date: data.Date,
//           programming: data.programming
//         });
//       })
//       .catch(error => console.error('Error fetching data:', error));
//   }, []); // Empty dependency array means this runs once when component mounts


//   return (
//     <>
//       <h1>cheap bananas</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>{data.name}</p>
//         <p>{data.age}</p>
//         <p>{data.date}</p>
//         <p>{data.programming}</p>
//       </div>
//     </>
//   )
// }

// export default App
