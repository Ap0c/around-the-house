// ----- Setup ----- //

var errMessage = document.getElementById('err-message');
var form = document.getElementById('item-form');


// ----- Functions ----- //

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
		var requestParams = {
			route: buildUrl(...fields),
			method: 'POST',
			expectedStatus: 201
		};

		ajax(requestParams, function (success, result) {

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
