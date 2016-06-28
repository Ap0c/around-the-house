// ----- Setup ----- //

var resultsSection = document.getElementById('results');
var searchField = document.getElementById('search-field');
var form = document.getElementById('search-form');


// ----- Functions ----- //

// Builds the querystring-based search url.
function buildUrl (searchTerms) {
	return `/search?terms=${searchTerms}`;
}

// Handles the ajax response.
function responseHandler (success, result) {

	if (success) {
		resultsSection.innerHTML = results;
	} else {
		alert('Internal server Error.');
	}

}

// Handles form submit event and displays results.
function setupEvents () {

	form.addEventListener('submit', function (event) {

		event.preventDefault();

		var searchTerms = searchField.value;
		var requestParams = {
			route: buildUrl(searchTerms),
			method: 'GET',
			expectedStatus: 200
		};

		ajax(requestParams, responseHandler);

	});

}


// ----- Main ----- //

setupEvents();
