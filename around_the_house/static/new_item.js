// ----- Setup ----- //

var errMessage = document.getElementById('err-message');
var form = document.getElementById('item-form');


// ----- Functions ----- //

// Retrieves the item data from the form.
function getFields () {

	return {
		title: form.elements.title.value,
		author: form.elements.author.value,
		location: form.elements.location.value
	};

}

// Handles the ajax response.
function responseHandler (success, result) {

	if (success) {
		window.location = `/item/${result}`;
	} else {
		errMessage.textContent = result;
	}

}

// Handles form submit event and displays results.
function setupEvents () {

	form.addEventListener('submit', function (event) {

		event.preventDefault();

		var requestParams = {
			route: '/new_item',
			method: 'POST',
			expectedStatus: 201
		};

		ajax(requestParams, responseHandler, getFields());

	});

}


// ----- Run ----- //

setupEvents();
