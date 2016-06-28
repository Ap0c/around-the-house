// ----- Setup ----- //

var errMessage = document.getElementById('err-message');
var form = document.getElementById('item-form');


// ----- Functions ----- //

// Retrieves the item data from the form.
function getFields () {

	return [form.elements.id.value, form.elements.title.value,
		form.elements.author.value, form.elements.location.value];

}

// Builds the querystring-based search url.
function buildUrl (id, title, author, location) {
	return `/edit/${id}?title=${title}&author=${author}&location=${location}`;
}

// Handles form submit event and displays results.
function setupEvents () {

	form.addEventListener('submit', function (event) {

		event.preventDefault();

		var fields = getFields();
		var requestParams = {
			route: buildUrl(...fields),
			method: 'PUT',
			expectedStatus: 200
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
