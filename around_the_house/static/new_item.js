// ----- Setup ----- //

var errMessage = document.getElementById('err-message');
var form = document.getElementById('item-form');


// ----- Functions ----- //

// Retrieves the item data from the form.
function getFields () {

	return Array.from(form.elements).reduce(gatherFields, {});

	function gatherFields (fields, field) {

		if (field.name) {
			fields[field.name] = field.value;
		}

		return fields;

	}

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
			route: '/new_item',
			method: 'POST',
			expectedStatus: 201
		};

		ajax(requestParams, responseHandler, fields);

	});

}


// ----- Run ----- //

setupEvents();
