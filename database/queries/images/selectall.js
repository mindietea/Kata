var mysql = require('mysql');
require('dotenv').load();

var connection = mysql.createConnection({
  host     : process.env.HOST,
  user     : process.env.USER,
  password : process.env.PASSWORD,
  port     : process.env.PORT,
  database : "ImageDB"
});

connection.connect(function(err) {
  if (err) {
    console.error('Database connection failed: ' + err.stack);
	connection.end()
    return;
  }

  console.log('Connected to database.');
  var query = "SELECT * FROM images"
  console.log("running query \"" + query + "\"...");
  connection.query(query, function(error, result){
	  console.log("The result is " + JSON.stringify(result))
  });
  connection.end()
});
