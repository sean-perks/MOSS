/* 
	Student Name: Sean Perks
	File Name: script.js
	Date: 8/11/2024
*/

// Hamburger menu Function
function hamburger () {
	var menu = document.getElementById("menu-links");
	var logo = document.getElementById("logo");
	if (menu.style.display === "block" && logo.style.display === "none") {
		menu.style.display = "none";
		logo.style.display = "block";
	} else {
		menu.style.display = "block";
		logo.style.display = "none";
	}
}

const map = L.map('map').setView([45.5, -122], 6.3); // Initialize the map at a default location

// Load and display tile layers
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);

// Marker variable
let marker;

// Function to display a marker and zoom to it
function displayMarker(lat, lon) {
    if (marker) {
        map.removeLayer(marker); // Remove existing marker
    }
    // Load and display tile layers
    L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 20,
        attribution: 'Tiles &copy; Esri &mdash; Source: US Geological Survey',
    }).addTo(map);
    // Define custom marker icon
    const customIcon = L.icon({
    	iconUrl: 'static/cow_logo_evil.png', // Replace with your icon URL
        iconSize: [38, 38], // Size of the icon
        iconAnchor: [19, 38], // Point of the icon which will correspond to marker's location (center bottom)
        popupAnchor: [0, -38] // Point from which the popup should open relative to the iconAnchor
    });
    marker = L.marker([lat, lon], {icon: customIcon }).addTo(map).bindPopup(`Here you point!`).openPopup();
    map.setView([lat, lon], 13); // Zoom into the displayed marker
}



// Handle map click events
map.on('click', function(e) {
    const lat = e.latlng.lat;
    const lon = e.latlng.lng;

    // Update hidden form fields with selected coordinates
    document.getElementById('lat').value = lat;
    document.getElementById('lon').value = lon;

    // Add a marker on the map
    if (marker) {
        map.removeLayer(marker); // Remove previous marker
    }
    marker = L.marker([lat, lon]).addTo(map).bindPopup(`Lat: ${lat}, Lon: ${lon}`).openPopup();
});