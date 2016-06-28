// ----- Setup ----- //

var deleteLink = document.getElementById('delete-link');


// ----- Functions ----- //

// Handles form submit event and displays results.
function setupEvents () {

	deleteLink.addEventListener('click', function (event) {

		event.preventDefault();

		var requestParams = {
			route: event.target.getAttribute('href'),
			method: 'DELETE',
			expectedStatus: 204
		};

		ajax(requestParams, function () {
			window.location = '/';
		});

	});

}


// ----- Run ----- //

setupEvents();
