// ----- Functions ----- //

// Posts JSON data to a specified route, and fires callback with result.
function jsonPost (route, callback) {

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


// ----- Main ----- //


