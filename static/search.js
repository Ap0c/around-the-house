// ----- Setup ----- //

var resultsSection = document.getElementById('results');
var searchField = document.getElementById('search-field');
var form = document.getElementById('search-form');


// ----- Functions ----- //

// Posts JSON data to a specified route, and fires callback with result.
function jsonGet (route, callback) {

	var ajaxRequest = new XMLHttpRequest();

	ajaxRequest.onreadystatechange = function ajaxChange () {

		if (ajaxRequest.readyState == XMLHttpRequest.DONE) {

			if (ajaxRequest.status === 200) {
				callback(ajaxRequest.responseText);
			} else {
				alert('Internal server Error.');
			}

		}

	};

	ajaxRequest.open('GET', route);
	ajaxRequest.send();

}


// Builds the querystring-based search url.
function buildUrl (searchTerms) {
	return `/search?terms=${searchTerms}`;
}


// Handles form submit event and displays results.
function setupEvents () {

	form.addEventListener('submit', function (event) {

		event.preventDefault();

		var searchTerms = searchField.value;
		var url = buildUrl(searchTerms);

		jsonGet(url, function (results) {
			console.log(results);
			resultsSection.innerHTML = results;
		});

	});

}


// ----- Main ----- //

setupEvents();
