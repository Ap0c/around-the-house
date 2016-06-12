// ----- Setup ----- //

var deleteLink = document.getElementById('delete-link');


// ----- Functions ----- //

// Sends a delete request to a specific route, and fires callback with result.
function jsonDelete (route, callback) {

	var ajaxRequest = new XMLHttpRequest();

	ajaxRequest.onreadystatechange = function ajaxChange () {

		if (ajaxRequest.readyState == XMLHttpRequest.DONE) {

			if (ajaxRequest.status === 204) {
				callback(ajaxRequest.responseText);
			} else {
				alert('Internal server Error.');
			}

		}

	};

	ajaxRequest.open('DELETE', route);
	ajaxRequest.send();

}


// Handles form submit event and displays results.
function setupEvents () {

	deleteLink.addEventListener('click', function (event) {

		event.preventDefault();

		var url = event.target.getAttribute('href');

		jsonDelete(url, function () {
			window.location = '/';
		});

	});

}


// ----- Run ----- //

setupEvents();
