module.exports = function(){
  var express = require('express');
  var session = require('express-session');
  var MySQLStore = require('express-mysql-session')(session);
  var bodyParser = require('body-parser');
  var path = require('path');
  var app = express();
  var sassMiddleware = require('node-sass-middleware');
  app.use(sassMiddleware({
    src: './public',
    dest: './public',
    indentedSyntax: true, // true = .sass and false = .scss
    sourceMap: true
  }));
  app.use(express.static('./public'));


  app.set('views', './view');           // New!!
  app.set('view engine', 'ejs');
  app.use(bodyParser.urlencoded({ extended: false }));
  app.use(session({
    secret: '19q0iojd0129ijrol!',
    resave: false,
    saveUninitialized: true,
    cookie: {
      maxAge: 1000 * 60 * 60 // 쿠키 유효기간 1시간
    },
    store:new MySQLStore({
      host:'localhost',
      port: 9000,
      user:'root',
      password:'1q2w3e',
      database:'capstonedb'
    })
  }));

  return app;
}
