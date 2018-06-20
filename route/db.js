module.exports = function(){

  //User 만 autoincrement 해주기
  var mysql = require('mysql');
  var conn = mysql.createConnection({
    host :'localhost',
    user :'root',
    password :'1234',
    database :'capstonedb'
  });
  conn.connect();
  return conn;
}
