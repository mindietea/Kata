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
  var query = "CREATE TABLE posts (PostID int NOT NULL AUTO_INCREMENT, Curator varchar(255), Date varchar(255), Title varchar(255), Description varchar(10000), PRIMARY KEY (PostID));"
  console.log("running query \"" + query + "\"...");
  connection.query(query);
  connection.end()
});
