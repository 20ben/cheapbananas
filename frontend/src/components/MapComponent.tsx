import { useEffect, useRef, useState } from "react";

// Declare global google object and types
type GoogleMap = {
	panTo: (location: MapLocation) => void;
	setZoom: (zoom: number) => void;
	getZoom: () => number;
	fitBounds: (bounds: unknown) => void;
	addListener: (event: string, handler: (e?: unknown) => void) => void;
	setOptions: (options: unknown) => void;
};

type GoogleMarker = {
	setMap: (map: GoogleMap | null) => void;
};

declare global {
	interface Window {
		google: {
			maps: {
				Map: new (element: HTMLElement, options: unknown) => GoogleMap;
				Marker: new (options: unknown) => GoogleMarker;
				Circle: new (options: unknown) => { getBounds: () => unknown };
				LatLngBounds: new () => {
					extend: (location: MapLocation) => void;
				};
				ControlPosition: { TOP_RIGHT: number };
				SymbolPath: { CIRCLE: number };
			};
		};
		initMap: () => void;
	}
}

// Google Maps API Key - Replace with your own key
const MAPS_API_KEY = "AIzaSyAn4h2aJ5gzIUxOdaxun2I01Y_rpl4Vd3Q";

// Map configuration
const MAP_RADIUS = 20000;

export type MapLocation = {
	lat: number;
	lng: number;
};

type MarkerLocation = MapLocation & {
	name?: string;
};

type PlaceResult = {
	name?: string;
	geometry?: {
		location: MapLocation;
	};
};

type MapComponentProps = {
	center?: MapLocation;
	onLocationSearch?: (location: MapLocation) => void;
	selectedPlace?: PlaceResult | null;
	markers?: MarkerLocation[];
};

// Load Google Maps script
function loadGoogleMapsScript(): Promise<void> {
	return new Promise((resolve, reject) => {
		// Check if already loaded
		if (window.google?.maps) {
			resolve();
			return;
		}

		const script = document.createElement("script");
		script.src = `https://maps.googleapis.com/maps/api/js?key=${MAPS_API_KEY}&libraries=places,geometry&callback=initMap`;
		script.async = true;
		script.defer = true;

		window.initMap = () => {
			resolve();
		};

		script.onerror = () => {
			reject(new Error("Failed to load Google Maps script"));
		};

		document.head.appendChild(script);
	});
}

export function MapComponent({
	center: initialCenter,
	onLocationSearch,
	selectedPlace,
	markers = [],
}: MapComponentProps) {
	const mapRef = useRef<HTMLDivElement>(null);
	const [map, setMap] = useState<GoogleMap | null>(null);
	const [userLocation, setUserLocation] = useState<MapLocation | null>(null);
	const markersRef = useRef<GoogleMarker[]>([]);
	const selectedMarkerRef = useRef<GoogleMarker | null>(null);

	// Get user's current location on mount
	useEffect(() => {
		if ("geolocation" in navigator) {
			navigator.geolocation.getCurrentPosition(
				(position) => {
					const location = {
						lat: position.coords.latitude,
						lng: position.coords.longitude,
					};
					setUserLocation(location);
				},
				(error) => {
					console.warn("Geolocation failed:", error.message);
					// Fallback to default location (San Francisco)
					setUserLocation({ lat: 37.8715, lng: -122.273 });
				},
			);
		} else {
			setUserLocation({ lat: 37.8715, lng: -122.273 });
		}
	}, []);

	// Initialize Google Maps
	useEffect(() => {
		if (!mapRef.current || !userLocation) return;

		loadGoogleMapsScript()
			.then(() => {
				const google = window.google;
				const center = initialCenter || userLocation;

				const mapBounds = new google.maps.Circle({
					center,
					radius: MAP_RADIUS,
				}).getBounds();

				if (!mapRef.current) return;

				const mapInstance = new google.maps.Map(mapRef.current, {
					center,
					zoom: 18,
					restriction: { latLngBounds: mapBounds || undefined },
					mapTypeControl: true,
					mapTypeControlOptions: {
						position: google.maps.ControlPosition.TOP_RIGHT,
					},
					fullscreenControl: true,
					streetViewControl: false,
					zoomControl: true,
					maxZoom: 22,
					minZoom: 12,
				});

				// Add click listener for POI pins
				mapInstance.addListener("click", (e?: unknown) => {
					const event = e as { placeId?: string; stop?: () => void };
					if (event.placeId) {
						event.stop?.();
						// Handle place selection
						console.log("Selected place ID:", event.placeId);
					}
				});

				// Customize map styling based on zoom level
				mapInstance.addListener("zoom_changed", () => {
					const hideDefaultPoiPins = (mapInstance.getZoom() || 0) < 18;
					mapInstance.setOptions({
						styles: [
							{
								featureType: "poi",
								elementType: hideDefaultPoiPins ? "labels" : "labels.text",
								stylers: [{ visibility: "off" }],
							},
						],
					});
				});

				setMap(mapInstance);
			})
			.catch((error) => {
				console.error("Failed to initialize Google Maps:", error);
			});
	}, [userLocation, initialCenter]);

	// Add markers to map
	useEffect(() => {
		if (!map) return;

		const google = window.google;

		// Clear existing markers
		for (const marker of markersRef.current) {
			marker.setMap(null);
		}
		markersRef.current = [];

		// Add new markers
		for (const location of markers) {
			const marker = new google.maps.Marker({
				position: { lat: location.lat, lng: location.lng },
				map: map,
				title: location.name || `Location: ${location.lat}, ${location.lng}`,
				icon: {
					path: google.maps.SymbolPath.CIRCLE,
					scale: 8,
					fillColor: "red",
					fillOpacity: 1,
					strokeWeight: 1,
					strokeColor: "darkred",
				},
			});

			markersRef.current.push(marker);
		}

		// Fit bounds to include all markers
		if (markers.length > 0) {
			const bounds = new google.maps.LatLngBounds();
			for (const location of markers) {
				bounds.extend({ lat: location.lat, lng: location.lng });
			}
			map.fitBounds(bounds);
		}
	}, [map, markers]);

	// Update selected place marker
	useEffect(() => {
		if (!map || !selectedPlace?.geometry?.location) return;

		const google = window.google;

		// Remove previous selected marker
		if (selectedMarkerRef.current) {
			selectedMarkerRef.current.setMap(null);
		}

		// Add new selected marker
		const marker = new google.maps.Marker({
			position: selectedPlace.geometry.location,
			map: map,
			title: selectedPlace.name || "Selected Place",
		});

		selectedMarkerRef.current = marker;

		// Pan to selected location
		map.panTo(selectedPlace.geometry.location);
		map.setZoom(18);
	}, [map, selectedPlace]);

	// Handle current location button click
	const handleCurrentLocation = () => {
		if (!map) return;

		if ("geolocation" in navigator) {
			navigator.geolocation.getCurrentPosition(
				(position) => {
					const location = {
						lat: position.coords.latitude,
						lng: position.coords.longitude,
					};
					map.panTo(location);
					map.setZoom(18);

					// Notify parent component
					if (onLocationSearch) {
						onLocationSearch(location);
					}
				},
				(error) => {
					alert(`Could not get location: ${error.message}`);
				},
			);
		} else {
			alert("Geolocation is not supported by this browser.");
		}
	};

	return (
		<div className="relative w-full h-full">
			<div ref={mapRef} className="w-full h-full" />

			{/* Current Location Button */}
			<button
				type="button"
				onClick={handleCurrentLocation}
				className="absolute bottom-6 right-6 bg-white rounded-full p-3 shadow-lg hover:bg-gray-50 transition-colors"
				title="Current Location"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					width="24"
					height="24"
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					strokeWidth="2"
					strokeLinecap="round"
					strokeLinejoin="round"
				>
					<title>Current Location</title>
					<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z" />
					<circle cx="12" cy="10" r="3" />
				</svg>
			</button>
		</div>
	);
}
