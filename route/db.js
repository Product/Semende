module.exports = function(){

  //User 만 autoincrement 해주기
  var mysql = require('mysql');
  var conn = mysql.createConnection({
    host :'localhost',
    user :'root',
    port :'9000',
    password :'1q2w3e',
    database :'capstonedb'
  });
  conn.connect();
  return conn;
}
