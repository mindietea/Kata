var mysql = require('mysql');
require('dotenv').load();

var connection = mysql.createConnection({
  host     : process.env.HOST,
  user     : process.env.USER,
  password : process.env.PASSWORD,
  port     : process.env.PORT,
  database : process.env.DATABASE,
});

connection.connect(function(err) {
  if (err) {
    console.error('Database connection failed: ' + err.stack);
	connection.end()
    return;
  }

  console.log('Connected to database.');
  var query = "CREATE TABLE products (PostID int, ProductLink varchar(255), ProductName varchar(255), InStock ENUM('false', 'true'), sizes varchar(500));"
  console.log("running query \"" + query + "\"...");
  connection.query(query);
  connection.end()
});
