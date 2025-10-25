import React, { useState } from "react";
import MapView from "./MapView.jsx";

export default function App() {
  const [userLocation, setUserLocation] = useState(null);
  const [error, setError] = useState(null);

  const handleGetLocation = () => {
    if (!navigator.geolocation) {
      setError("Geolocation is not supported by your browser.");
      return;
    }

    navigator.geolocation.getCurrentPosition(
      (position) => {
        const coords = {
          latitude: position.coords.latitude,
          longitude: position.coords.longitude,
        };
        setUserLocation(coords);
        setError(null);
        console.log("User location:", coords);
      },
      (err) => {
        switch (err.code) {
          case err.PERMISSION_DENIED:
            setError("User denied the request for Geolocation.");
            break;
          case err.POSITION_UNAVAILABLE:
            setError("Location information is unavailable.");
            break;
          case err.TIMEOUT:
            setError("The request to get user location timed out.");
            break;
          default:
            setError("An unknown error occurred.");
        }
      }
    );
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        height: "100vh", // full viewport height
      }}
    >
      {/* HEADER */}
      <div
        style={{
          backgroundColor: "#f8f8f8",
          padding: "10px 15px",
          boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
          zIndex: 1000,
          flexShrink: 0, // prevents shrinking
        }}
      >
        <h1 style={{ marginBottom: "8px" }}>CheapBananas Map</h1>

        <button
          onClick={handleGetLocation}
          style={{
            padding: "8px 16px",
            backgroundColor: "#2563eb",
            color: "white",
            border: "none",
            borderRadius: "6px",
            cursor: "pointer",
            marginRight: "10px",
          }}
        >
          Request My Location
        </button>

        {userLocation && (
          <span>
            📍 {userLocation.latitude.toFixed(4)},{" "}
            {userLocation.longitude.toFixed(4)}
          </span>
        )}

        {error && <p style={{ color: "red", marginTop: "5px" }}>{error}</p>}
      </div>

      {/* MAP SECTION */}
      <div style={{ flexGrow: 1, minHeight: 0 }}>
        <MapView userLocation={userLocation} />
      </div>
    </div>
  );
}
