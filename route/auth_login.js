module.exports = function(passport){
  var bkfd2Password = require("pbkdf2-password");
  var hasher = bkfd2Password();
  var conn = require('./db')();
  var conn2 = require('./db')();
  var route = require('express').Router();
  var PythonShell = require('python-shell');


  route.post(
    '/login',
    passport.authenticate(
      'local',
      {
        successRedirect: '/mypage',
        failureRedirect: '/login_error',
        failureFlash: false
      }
    )
  );


  route.post('/register', function(req, res){
     hasher({password:req.body.password}, function(err, pass, salt, hash){
       var user = {
         ID :'local:'+req.body.username,
         Password:hash,
         Username:req.body.displayName,
         Gender:req.body.gender,
         Job:req.body.job,
         Age:req.body.age,
         Salt:salt,
         Email:req.body.email
       };
       var sql = 'INSERT INTO User SET ?';
       conn.query(sql, user, function(err, results){
         if(err){
           console.log(err);
           res.status(500);
         } else {
           req.login(user, function(err){
             req.session.save(function(){
               res.redirect('/mypage');
             });
           });
         }
       });
     });
   }
 );

 //ID 중복체zm
 route.post('/id_check', function(req, res){
   var id = req.body.username;
   var sql = "select *  from user WHERE ID = 'local:"+id+"';"
   conn.query(sql,function(err, results){
     if(err){
       console.log(err);
       res.status(500);
     } else {
       //일치하는것이 없는경우
       if(results[0]==undefined){
         //세션에 사용가능한 아이디 저장
         req.session.username=id;
         res.redirect('/register_checked');
       }
       else{
        res.redirect('/popup_id_check_error');
       }
     }
   });


 });

 route.post('/pw_check', function(req, res){
   hasher({password:req.body.password, salt:req.user.Salt}, function(err, pass, salt, hash){

     var sql = 'SELECT Password from User where User_id= ? ';
     conn.query(sql, [req.user.User_id], function(err, results){
       if(err){
         console.log(err);
         res.status(500);
       } else {
         if(results[0].Password===hash){
             res.redirect('/User_info_modify');
         }
         else{
           res.redirect('/password_input_error')
         }

       }
     });
   });
 });

 route.post('/update', function(req, res){
    hasher({password:req.body.password}, function(err, pass, salt, hash){

      var sql = 'UPDATE User SET Password = ?, Salt =? , Email =?  where User_id= ? ';
      conn.query(sql, [hash, salt, req.body.email, req.user.User_id], function(err, results){
        if(err){
          console.log(err);
          res.status(500);
        } else {
              res.redirect('/mypage');
        }
      });
    });
  }
);


//면세점 연동 - 롯데


route.post('/lottemembership', function(req, res){
    //DB관련 문제 해결 필요 User_info_id
     var user = {
       User_info_id : req.user.User_id,
       Shilla_id : null,
       Shilla_pw: null,
       Shinsegae_id : null,
       Shinsegae_pw: null,
       Lotte_id :req.body.username,
       Lotte_pw:req.body.password,
       User_id : req.user.User_id
     };
     //python에 보낼 사용자 인증정보 설정
     var options={
       mode: 'text',
      pythonPath: '',
      pythonOptions: ['-u'],
      scriptPath: '',
      args: [req.body.username,req.body.password]
     }
     PythonShell.run('./python/authDutyfree/checkLotteID.py', options, function (err, results) {
       if (err) throw err;

        if(results=='lotte success'){
          var sql = 'INSERT INTO User_info SET ?';
          var upsql = 'UPDATE User_info SET Lotte_id = ?, Lotte_pw =?, User_id =?  WHERE User_info_id=?'

          conn.query(sql, user, function(err, results){
            if(err){
              console.log(err);
              conn2.query(upsql,[req.body.username,req.body.password,req.user.User_id,req.user.User_id],function(err, results){
                if(err){
                  console.log("Update error "+ user_id + "'s" + err);
                      res.redirect('/popup_lotte');
                }
                else{
                      res.redirect('/popup_success');
                }
              });
            } else {
                  res.redirect('/popup_success');
            }
          });



          //만일 기존에 연동된 토큰이 있다면 UPDATE 실행

        }
        else{
          res.redirect('/popup_lotte_error');
        }
     });
 }
);

//면세점 연동 - 신라


route.post('/shinlamembership', function(req, res){

     var user = {
       User_info_id : req.user.User_id,
       Shilla_id : req.body.username,
       Shilla_pw: req.body.password,
       Shinsegae_id : null,
       Shinsegae_pw: null,
       Lotte_id : null,
       Lotte_pw: null,
       User_id : req.user.User_id
     };
     //python에 보낼 사용자 인증정보 설정
     var options={
       mode: 'text',
      pythonPath: '',
      pythonOptions: ['-u'],
      scriptPath: '',
      args: [req.body.username,req.body.password]
     }
     PythonShell.run('./python/authDutyfree/checkShinlaID.py', options, function (err, results) {
       if (err) throw err;

        if(results=='shinla success'){
          var sql = 'INSERT INTO User_info SET ?';
          var upsql = 'UPDATE User_info SET Shilla_id = ?, Shilla_pw =?, User_id =? WHERE User_info_id=?'
          conn.query(sql, user, function(err, results){
            if(err){
              console.log(err);
              res.status(500);
              conn2.query(upsql,[req.body.username,req.body.password,req.user.User_id,req.user.User_id],function(err, results){
                if(err){
                  console.log("Update error "+ user_id + "'s" + err);
                      res.redirect('/popup_shilla');
                }
                else{
                      res.redirect('/popup_success');
                }
              });

            } else {
                  res.redirect('/popup_success');
            }
          });
          //update 문 실행후 만약 없으면 create 문 실행

        }
        else{
          res.redirect('/popup_shilla_error');
        }
     });
 }
);


//면세점 연동 - 신세계


route.post('/ssgmembership', function(req, res){

     var user = {
       User_info_id : req.user.User_id,
       Shilla_id : null,
       Shilla_pw: null,
       Shinsegae_id : req.body.username,
       Shinsegae_pw: req.body.password,
       Lotte_id : null,
       Lotte_pw: null,
       User_id : req.user.User_id
     };
     //python에 보낼 사용자 인증정보 설정
     var options={
       mode: 'text',
      pythonPath: '',
      pythonOptions: ['-u'],
      scriptPath: '',
      args: [req.body.username,req.body.password]
     }
     PythonShell.run('./python/authDutyfree/checkShinsaegaeID.py', options, function (err, results) {
       if (err) throw err;
        console.log(results);
        if(results=='ssg success'){
          var sql = 'INSERT INTO User_info SET ?';
          var upsql = 'UPDATE User_info SET Shinsegae_id = ?, Shinsegae_pw =?, User_id=? WHERE User_info_id=?'
          conn.query(sql, user, function(err, results){
            if(err){
              console.log(err);
              //만일 기존에 연동된 토큰이 있다면 UPDATE 실행
              conn2.query(upsql,[req.body.username,req.body.password,req.user.User_id,req.user.User_id],function(err, results){
                if(err){
                  console.log("Update error "+ user_id + "'s" + err);
                  res.redirect('/popup_shinsegae');
                }
                else{
                      res.redirect('/popup_success');
                }
              });
              res.status(500);
            } else {
                  res.redirect('/popup_success');
            }
          });

        }
        else{
          res.redirect('/popup_shinsegae_error');
        }
     });
 }
);

   // route.get('/lotte', function(req, res){
   //   res.render('lotteauth',{errormsg :""});
   // });
   // route.get('/shinla', function(req, res){
   //   res.render('shinlaauth',{errormsg :""});
   // });
   // route.get('/ssg', function(req, res){
   //   res.render('ssgauth',{errormsg :""});
   // });

   // route.get('/register', function(req, res){
   //   res.render('register');
   // });
   // route.get('/login', function(req, res){
   //   res.render('login');
   // });
   route.get('/logout', function(req, res){
     req.logout();
     //구글 logout 해야된다.
     req.session.save(function(){
       res.redirect('/index');
     });
   });
   return route;

}
