// ----- Functions ----- //

// Posts JSON data to a specified route, and fires callback with result.
function ajax (request, callback, data) {

	var ajaxRequest = new XMLHttpRequest();

	ajaxRequest.addEventListener('load', function () {

		var success = ajaxRequest.status === request.expectedStatus;
		var responseType = ajaxRequest.getResponseHeader('Content-Type');
		var result = null;

		if (responseType === 'application/json') {
			result = JSON.parse(ajaxRequest.responseText);
		} else {
			result = ajaxRequest.responseText;
		}

		callback(success, result);

	});

	ajaxRequest.addEventListener('error', function (err) {
		callback(false, 'Network problem.');
	});

	ajaxRequest.open(request.method, request.route, true);

	if (data) {

		ajaxRequest.setRequestHeader('Content-Type', 'application/json');
		ajaxRequest.send(JSON.stringify(data));

	} else {
		ajaxRequest.send();
	}

}
