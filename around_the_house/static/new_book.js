// ----- Setup ----- //

var errMessage = document.getElementById('err-message');
var form = document.getElementById('item-form');


// ----- Functions ----- //

// Posts JSON data to a specified route, and fires callback with result.
function jsonPost (route, callback) {

	var ajaxRequest = new XMLHttpRequest();

	ajaxRequest.onreadystatechange = function ajaxChange () {

		if (ajaxRequest.readyState == XMLHttpRequest.DONE) {

			if (ajaxRequest.status === 201) {
				callback(true, ajaxRequest.responseText);
			} else {
				callback(err);
			}

		}

	};

	ajaxRequest.open('POST', route);
	ajaxRequest.send();

}

// Retrieves the item data from the form.
function getFields () {

	return [form.elements.title.value, form.elements.author.value,
	form.elements.location.value];

}

// Builds the querystring-based search url.
function buildUrl (title, author, location) {
	return `/new_item?title=${title}&author=${author}&location=${location}`;
}

// Handles form submit event and displays results.
function setupEvents () {

	form.addEventListener('submit', function (event) {

		event.preventDefault();

		var fields = getFields();
		var url = buildUrl(...fields);

		jsonPost(url, function (success, result) {

			if (success) {
				window.location = `/item/${result}`;
			} else {
				errMessage.textContent = result;
			}
			
		});

	});

}


// ----- Run ----- //

setupEvents();
