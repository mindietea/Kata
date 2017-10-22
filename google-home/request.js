var request = require('request')
	var options = { method: 'GET',
 url: 'http://76b40d76.ngrok.io/api/post/recommendations/ghome',
 qs: { name: "potato" } };

request(options, function (error, response, body) {
 	body = JSON.parse(body)
	console.log(body['results'])
});
