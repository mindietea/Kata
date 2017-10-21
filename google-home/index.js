'use strict';

const ApiAiApp = require('actions-on-google').ApiAiApp

var request = require('request');
const WELCOME_INTENT = 'input.welcome'; //this is the name rom the API.AI intent. check the API.AI event console.

exports.kata = (req, res) => {
  const app = new ApiAiApp({ request: req, response: res});
  function welcomeIntent(app){
	  var options = { method: 'POST',
  	url: 'http://1094eb34.ngrok.io/getFood',
	formData: { food: String(app.data.input) } };

	request(options, function (error, response, body) {
		response = JSON.parse(response)
		if(response['results'].length > 0){
			if(response['results'].length > 3){
				app.tell(app.buildRichResponse().addSimpleResponse("Here are the top three results for your search: " + String(app.data.input))
				.addBasicCard(app.buildBasicCard('Result 1: ' + response['results'][0]['name'] + " Price: " + response['results'][0]['price'] + " Brand: " + response['results'][0]['brand']))
				.addButton('View on Amazon', response['results'][0]['url'])
				.setImage(response['results'][0]['image'])
				.addBasicCard(app.buildBasicCard('Result 2: ' + response['results'][1]['name'] + " Price: " + response['results'][1]['price'] + " Brand: " + response['results'][1]['brand']))
				.addButton('View on Amazon', response['results'][1]['url'])
				.setImage(response['results'][1]['image'])
				.addBasicCard(app.buildBasicCard('Result 3: ' + response['results'][2]['name'] + " Price: " + response['results'][2]['price'] + " Brand: " + response['results'][2]['brand']))
				.addButton('View on Amazon', response['results'][2]['url'])
				.setImage(response['results'][2]['image'])
				)
			}
			else{
				app.tell(app.buildRichResponse().addSimpleResponse("Here is the top result for your search: " + String(app.data.input))
				.addBasicCard(app.buildBasicCard('Result 1: ' + response['results'][0]['name'] + " Price: " + response['results'][0]['price'] + " Brand: " + response['results'][0]['brand']))
				.addButton('View on Amazon', response['results'][0]['url'])
				.setImage(response['results'][0]['image']))
			}
		}
		else{
			app.tell("No results found. Try again.")
		}
		});
  }


  let actionMap = new Map();
  actionMap.set(WELCOME_INTENT, welcomeIntent)
  app.handleRequest(actionMap);
}
