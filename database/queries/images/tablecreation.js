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
  var query = "CREATE TABLE images (PostID int, ImageLink varchar(255), ImageName varchar(255));"
  console.log("running query \"" + query + "\"...");
  connection.query(query);
  connection.end()
});
