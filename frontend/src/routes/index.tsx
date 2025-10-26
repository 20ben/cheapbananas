import { MapComponent, type MapLocation } from "@/components/MapComponent";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { createFileRoute } from "@tanstack/react-router";
import { Clock, MapPin, Navigation, Star } from "lucide-react";
import { useState } from "react";

export const Route = createFileRoute("/")({
	component: App,
});

// Location data type structure compatible with Flask backend integration
type Location = {
	id: string;
	name: string;
	category: string;
	address: string;
	rating: number;
	hours: string;
	imageUrl: string;
};

// Dummy JSON data for locations
const locationData: Location[] = [
	{
		id: "1",
		name: "Blue Bottle Coffee",
		category: "Cafe",
		address: "66 Mint St, San Francisco, CA 94103",
		rating: 4.5,
		hours: "Open · Closes 6:00 PM",
		imageUrl:
			"https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=100&h=100&fit=crop",
	},
	{
		id: "2",
		name: "Golden Gate Park",
		category: "Park",
		address: "Golden Gate Park, San Francisco, CA 94122",
		rating: 4.8,
		hours: "Open 24 hours",
		imageUrl:
			"https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=100&h=100&fit=crop",
	},
	{
		id: "3",
		name: "Ferry Building Marketplace",
		category: "Shopping",
		address: "1 Ferry Building, San Francisco, CA 94111",
		rating: 4.6,
		hours: "Open · Closes 7:00 PM",
		imageUrl:
			"https://images.unsplash.com/photo-1534452203293-494d7ddbf7e0?w=100&h=100&fit=crop",
	},
	{
		id: "4",
		name: "Tartine Bakery",
		category: "Bakery",
		address: "600 Guerrero St, San Francisco, CA 94110",
		rating: 4.7,
		hours: "Open · Closes 5:00 PM",
		imageUrl:
			"https://images.unsplash.com/photo-1509440159596-0249088772ff?w=100&h=100&fit=crop",
	},
	{
		id: "5",
		name: "Exploratorium",
		category: "Museum",
		address: "Pier 15, San Francisco, CA 94111",
		rating: 4.6,
		hours: "Open · Closes 5:00 PM",
		imageUrl:
			"https://images.unsplash.com/photo-1560264280-88b68371db39?w=100&h=100&fit=crop",
	},
	{
		id: "6",
		name: "Fisherman's Wharf",
		category: "Tourist Attraction",
		address: "Jefferson St, San Francisco, CA 94133",
		rating: 4.4,
		hours: "Open 24 hours",
		imageUrl:
			"https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=100&h=100&fit=crop",
	},
	{
		id: "7",
		name: "Zazie Restaurant",
		category: "Restaurant",
		address: "941 Cole St, San Francisco, CA 94117",
		rating: 4.5,
		hours: "Open · Closes 9:00 PM",
		imageUrl:
			"https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=100&h=100&fit=crop",
	},
	{
		id: "8",
		name: "Alamo Square Park",
		category: "Park",
		address: "Hayes St & Steiner St, San Francisco, CA 94117",
		rating: 4.7,
		hours: "Open 24 hours",
		imageUrl:
			"https://images.unsplash.com/photo-1519904981063-b0cf448d479e?w=100&h=100&fit=crop",
	},
];

function App() {
	// State management: Track which location is currently selected (null when none selected)
	const [selectedLocation, setSelectedLocation] = useState<Location | null>(
		null,
	);

	// State for map markers (locations returned from backend)
	const [mapMarkers, setMapMarkers] = useState<MapLocation[]>([]);

	// State for search input
	const [searchQuery, setSearchQuery] = useState("");

	/**
	 * Click handler for location list items
	 * Sets the selected location and triggers the detail panel to slide out
	 * @param location - The location object that was clicked
	 */
	const handleLocationClick = (location: Location) => {
		setSelectedLocation(location);
	};

	/**
	 * Close handler for detail panel
	 * Resets selected location to null, triggering slide-out animation
	 */
	const handleCloseDetail = () => {
		setSelectedLocation(null);
	};

	/**
	 * Handler for location search from map
	 * Called when user searches for a location or uses current location
	 */
	const handleLocationSearch = (location: MapLocation) => {
		// Here you would typically call your backend API
		// For now, we'll just add a sample marker
		console.log("Location searched:", location);

		// Example: Add sample markers around the searched location
		const sampleMarkers: MapLocation[] = [
			{ lat: location.lat + 0.001, lng: location.lng + 0.001 },
			{ lat: location.lat - 0.001, lng: location.lng - 0.001 },
			{ lat: location.lat + 0.002, lng: location.lng - 0.001 },
		];

		setMapMarkers(sampleMarkers);
	};

	return (
		<div className="flex h-screen bg-gray-100">
			{/* Sidebar: Fixed-width scrollable location list */}
			<div className="w-96 bg-white shadow-lg flex flex-col">
				{/* Search bar header */}
				<div className="p-4 border-b border-gray-200">
					<div className="flex items-center gap-2 px-3 py-2 bg-gray-50 rounded-lg">
						<MapPin className="w-5 h-5 text-gray-400" />
						<input
							type="text"
							placeholder="Search for places..."
							className="flex-1 bg-transparent outline-none text-sm"
							value={searchQuery}
							onChange={(e) => setSearchQuery(e.target.value)}
						/>
					</div>
				</div>

				{/* Scrollable location list with smooth overflow behavior */}
				<ScrollArea className="flex-1">
					<div className="divide-y divide-gray-200">
						{locationData.map((location) => (
							<LocationCard
								key={location.id}
								location={location}
								isSelected={selectedLocation?.id === location.id}
								onClick={() => handleLocationClick(location)}
							/>
						))}
					</div>
				</ScrollArea>
			</div>

			{/* Slide-out detail panel: Appears to the right of sidebar when location is selected */}
			<DetailPanel location={selectedLocation} onClose={handleCloseDetail} />

			{/* Interactive Google Maps area */}
			<div className="flex-1 relative">
				<MapComponent
					onLocationSearch={handleLocationSearch}
					markers={mapMarkers}
				/>
			</div>
		</div>
	);
}

/**
 * LocationCard Component
 * Displays individual location in the list with name, category badge, and thumbnail
 * Handles hover states and selected state styling
 */
function LocationCard({
	location,
	isSelected,
	onClick,
}: {
	location: Location;
	isSelected: boolean;
	onClick: () => void;
}) {
	return (
		<button
			type="button"
			onClick={onClick}
			className={`
				w-full p-4 cursor-pointer transition-all duration-200 text-left
				hover:bg-gray-50
				${isSelected ? "bg-blue-50 border-l-4 border-l-blue-500" : ""}
			`}
		>
			<div className="flex gap-3">
				{/* Location thumbnail image */}
				<img
					src={location.imageUrl}
					alt={location.name}
					className="w-16 h-16 rounded-lg object-cover shrink-0"
				/>

				{/* Location info: name and category */}
				<div className="flex-1 min-w-0">
					<h3 className="font-semibold text-gray-900 truncate">
						{location.name}
					</h3>
					<div className="mt-1">
						<Badge variant="secondary" className="text-xs">
							{location.category}
						</Badge>
					</div>
					<div className="flex items-center gap-1 mt-2 text-sm text-gray-600">
						<Star className="w-4 h-4 fill-yellow-400 text-yellow-400" />
						<span>{location.rating}</span>
					</div>
				</div>
			</div>
		</button>
	);
}

/**
 * DetailPanel Component
 * Slide-out panel that displays full details of selected location
 * Shows when location prop is not null, hides with slide animation when null
 * Displays location name, address, rating, hours, and action buttons
 */
function DetailPanel({
	location,
	onClose,
}: {
	location: Location | null;
	onClose: () => void;
}) {
	// Smooth slide-in/slide-out animation controlled by location state
	// translate-x-full hides panel off-screen, translate-x-0 slides it in
	return (
		<div
			className={`
				w-96 bg-white shadow-2xl rounded-l-2xl transition-transform duration-300 ease-in-out
				${location ? "translate-x-0" : "translate-x-full absolute right-0"}
			`}
		>
			{location && (
				<div className="h-screen flex flex-col">
					{/* Detail panel header with close button */}
					<div className="p-6 border-b border-gray-200">
						<div className="flex justify-between items-start">
							<div className="flex-1">
								<h2 className="text-2xl font-bold text-gray-900">
									{location.name}
								</h2>
								<Badge variant="outline" className="mt-2">
									{location.category}
								</Badge>
							</div>
							<Button
								variant="ghost"
								size="icon"
								onClick={onClose}
								className="shrink-0"
							>
								<span className="text-xl">×</span>
							</Button>
						</div>
					</div>

					{/* Location image */}
					<div className="w-full h-48 shrink-0">
						<img
							src={location.imageUrl}
							alt={location.name}
							className="w-full h-full object-cover"
						/>
					</div>

					{/* Location details: rating, hours, address */}
					<div className="flex-1 overflow-y-auto p-6 space-y-4">
						{/* Rating display with star icon */}
						<div className="flex items-center gap-2">
							<Star className="w-5 h-5 fill-yellow-400 text-yellow-400" />
							<span className="text-lg font-semibold">{location.rating}</span>
							<span className="text-gray-500 text-sm">Rating</span>
						</div>

						{/* Opening hours */}
						<div className="flex items-start gap-2">
							<Clock className="w-5 h-5 text-gray-600 mt-0.5" />
							<div>
								<p className="text-sm font-medium text-gray-900">Hours</p>
								<p className="text-sm text-gray-600">{location.hours}</p>
							</div>
						</div>

						{/* Address */}
						<div className="flex items-start gap-2">
							<MapPin className="w-5 h-5 text-gray-600 mt-0.5" />
							<div>
								<p className="text-sm font-medium text-gray-900">Address</p>
								<p className="text-sm text-gray-600">{location.address}</p>
							</div>
						</div>
					</div>

					{/* Action buttons footer */}
					<div className="p-6 border-t border-gray-200 space-y-2">
						<Button className="w-full" size="lg">
							<Navigation className="w-4 h-4" />
							View on Map
						</Button>
						<Button variant="outline" className="w-full" size="lg">
							Get Directions
						</Button>
					</div>
				</div>
			)}
		</div>
	);
}
