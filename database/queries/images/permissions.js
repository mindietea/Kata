
var mysql = require('mysql');
require('dotenv').load();

var connection = mysql.createConnection({
  host     : process.env.HOST,
  user     : process.env.USER,
  password : process.env.PASSWORD,
  port     : process.env.PORT,
});

connection.connect(function(err) {
  if (err) {
    console.error('Database connection failed: ' + err.stack);
	connection.end()
    return;
  }
  var query = "SELECT * FROM mysql.db"
  connection.query(query, function(error, result){
	  console.log("The result is " + JSON.stringify(result))
  })

  connection.end()
});
