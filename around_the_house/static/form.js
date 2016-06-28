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

// Builds the request params based on form type.
function getParams (fields) {

	if (form.dataset.edit) {

		return {
			route: `/edit/${fields.id}`,
			method: 'PUT',
			expectedStatus: 200
		};

	} else {

		return {
			route: '/new_item',
			method: 'POST',
			expectedStatus: 201
		};

	}

}

// Handles form submit event and displays results.
function setupEvents () {

	form.addEventListener('submit', function (event) {

		event.preventDefault();

		var fields = getFields();
		var requestParams = getParams(fields);

		ajax(requestParams, responseHandler, fields);

	});

}


// ----- Run ----- //

setupEvents();
