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