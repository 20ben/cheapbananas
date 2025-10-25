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
  return (
    <div>
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
