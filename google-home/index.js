'use strict';

const ApiAiApp = require('actions-on-google').ApiAiApp

var request = require('request');
const WELCOME_INTENT = 'input.welcome'; //this is the name rom the API.AI intent. check the API.AI event console.
const INPUT_INTENT = 'input.input'

exports.kata = (req, res) => {
  const app = new ApiAiApp({ request: req, response: res});
  function welcomeIntent(app){
	  app.ask("Welcome to Kata, Please say anything you'd like to buy.")
  }
  function inputIntent(app){
	  var options = { method: 'GET',
   url: 'http://76b40d76.ngrok.io/api/post/recommendations/ghome',
   qs: { name: encodeURI(app.data.input) } };

 request(options, function (error, response, body) {
	 body = JSON.parse(body)
   if(body['results'].length > 0){
   	if(body['results'].length > 3){
		app.askWithList(app.buildRichResponse()
		    .addSimpleResponse('Alright')
		    .addSuggestions(
		      [body['results'][0]['title'], body['results'][1]['title'], body['results'][2]['title']]),
		    // Build a list
		    app.buildList('Top Results on ' + app.data.input)
		    // Add the first item to the list
		    .addItems(app.buildOptionItem('Result 1',
		      ['math', 'math and prime', 'prime numbers', 'prime'])
		      .setTitle(body['results'][0]['url'])
		      .setDescription("Result 1: " + body['results'][0]['title'] + " Price: " + body['results'][0]['price'] + "\nURL:" + body['results'][0]['url'])
		      .setImage(body['results'][0]['image'], "Result 1"))
		    // Add the second item to the list
			.addItems(app.buildOptionItem('Result2',
 			 ['math', 'math and prime', 'prime numbers', 'prime'])
 			 .setTitle(body['results'][1]['url'])
 			 .setDescription("Result 2: " + body['results'][1]['title'] + " Price: " + body['results'][1]['price'] + "\nURL:" + body['results'][1]['url'])
 			 .setImage(body['results'][1]['image'], "Result 2"))
			 .addItems(app.buildOptionItem('Result 3',
  			 ['math', 'math and prime', 'prime numbers', 'prime'])
  			 .setTitle(body['results'][2]['url'])
  			 .setDescription("Result 3: " + body['results'][2]['title'] + " Price: " + body['results'][2]['price'] + "\nURL:" + body['results'][2]['url'])
  			 .setImage(body['results'][2]['image'], "Result 3"))
		  );
   	}
   	else{
		app.tell(app.buildRichResponse()
		.addSimpleResponse("Here are the top three results for your search: " + String(app.data.input))
   		.addBasicCard(app.buildBasicCard('Result 1: ' + body['results'][0]['title'] + " Price: " + body['results'][0]['price'])
		.addButton('View on Amazon', body['results'][0]['url'])
		.setImage(body['results'][0]['image'], "Result 1")))
   	}
   }
   else{
   	app.tell("No results found. Try again.")
   }
 });

  }

  let actionMap = new Map();
  actionMap.set(WELCOME_INTENT, welcomeIntent)
  actionMap.set(INPUT_INTENT, inputIntent)
  app.handleRequest(actionMap);
}
