// ----- Setup ----- //

var errMessage = document.getElementById('err-message');
var form = document.getElementById('item-form');
var optionalInputs = document.getElementById('optional-inputs');


// ----- Form Views ----- //

var views = (function () {

	// ----- Internal Properties ----- //

	var typeInput = document.getElementById('type-input');
	var specificInputs = {
		Book: ['author-template'],
		Video: ['video-format-template'],
		Music: ['artist-template', 'video-format-template'],
		Audiobook: ['author-template', 'audio-format-template']
	};

	// ----- Functions ----- //

	// Clears the media-type specific inputs from the form.
	function clearOptionals () {

		while (optionalInputs.firstChild) {
			optionalInputs.removeChild(optionalInputs.firstChild);
		}

	}

	// Adds media-type specific inputs to the form.
	function addOptionals (inputs) {

		var docFrag = document.createDocumentFragment();

		inputs.forEach(function (input) {

			var template = document.getElementById(input);
			var element = document.importNode(template.content, true);

			docFrag.appendChild(element);

		});

		clearOptionals();
		optionalInputs.appendChild(docFrag);

	}

	// Updates the fields based upon current media type selected.
	function updateInputs () {

		var type = typeInput.value;
		addOptionals(specificInputs[type]);

	}

	// ----- Setup ----- //

	updateInputs();
	typeInput.addEventListener('change', updateInputs);

})();


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
