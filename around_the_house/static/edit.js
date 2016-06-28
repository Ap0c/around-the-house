// ----- Setup ----- //

var errMessage = document.getElementById('err-message');
var form = document.getElementById('item-form');


// ----- Functions ----- //

// Retrieves the item data from the form.
function getFields () {

	return {
		id: form.elements.id.value,
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

		var fields = getFields();
		var requestParams = {
			route: `/edit/${fields.id}`,
			method: 'PUT',
			expectedStatus: 200
		};

		ajax(requestParams, responseHandler, fields);

	});

}


// ----- Run ----- //

setupEvents();
