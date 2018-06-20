
var app = require('./route/express')();

var conn = require('./route/db')();
var passport = require('./route/passport')(app);
var getEvent = require('./route/getEvent');

app.get('/', function(req, res){
     res.send('Hello World')
});

// app.login('/login', function(req, res){
//      res.send('<h1>please login</h1>')
// })

app.listen(3030, function(){
     console.log("Connected 3030 port!")
});

app.get('/index', function(req, res){
  //로그인 되어있는지 안되어있는지 구분하기 위한 값
  var u_name;

  if(req.user == undefined){
      u_name='';
      res.render('index',{username: u_name});
  }
  else{
    u_name = req.user.Username
      res.render('index',{username: u_name});
  }

});

//신라 이벤트 페이지
app.get('/reserve_shilla', function(req, res){
  //신라 이벤트 페이지 csv로 받아오기
  getEvent("shillaPoint",function(eventlist_sl){
    var u_name;
    if(req.user == undefined){
        u_name='';

        res.render('reserve_shilla',{username: u_name, eventlist : eventlist_sl});
    }
    else{
      u_name = req.user.Username
        res.render('reserve_shilla',{username: u_name, eventlist : eventlist_sl});
    }
  });
  //로그인 되어있는지 안되어있는지 구분하기 위한 값

});
//lotte event page
app.get('/reserve_lotte', function(req, res){
  //로그인 되어있는지 안되어있는지 구분하기 위한 값
  getEvent("lottePoint",function(eventlist_sl){
    var u_name;
    if(req.user == undefined){
        u_name='';

        res.render('reserve_lotte',{username: u_name, eventlist : eventlist_sl});
    }
    else{
      u_name = req.user.Username
        res.render('reserve_lotte',{username: u_name, eventlist : eventlist_sl});
    }
  });

});

//ssg event page
app.get('/reserve_shinsegae', function(req, res){
  //로그인 되어있는지 안되어있는지 구분하기 위한 값
  getEvent("ssgPoint",function(eventlist_sl){
    var u_name;
    if(req.user == undefined){
        u_name='';

        res.render('reserve_shinsegae',{username: u_name, eventlist : eventlist_sl});
    }
    else{
      u_name = req.user.Username
        res.render('reserve_shinsegae',{username: u_name, eventlist : eventlist_sl});
    }
  });

});

app.get('/login_error', function(req, res){
  var u_name;
  if(req.user == undefined){
      u_name='';
        res.render('login',{username: u_name, errormsg : '아이디와 비밀번호를 확인하세요'});
  }
  else{
    u_name = req.user.Username
        res.render('login',{username: u_name, errormsg : '아이디와 비밀번호를 확인하세요'});
  }


});

app.get('/mypage', function(req, res ){
  console.log();
  if(req.user && req.user.Username) {
    res.render('mypage',{
      username: req.user.Username,
      Email: req.user.Email
    });

  }
  else res.render('index',{username: ''});
});
app.get('/register_checked',function(req, res){
  var u_name;
  if(req.user == undefined){
      u_name='';
      res.render('register',{username: u_name, username_check : req.session.username});
  }
  else{
    u_name = req.user.Username
      res.render('register',{username: u_name, username_check : req.session.username});
  }

});

app.get('/register',function(req, res){
  var u_name;
  if(req.user == undefined){
      u_name='';
      res.render('register',{username: u_name, username_check : ''});
  }
  else{
    u_name = req.user.Username
      res.render('register',{username: u_name, username_check : ''});
  }

});

app.get('/login',function(req, res){
  var u_name;
  if(req.user == undefined){
      u_name='';
      res.render('login',{username: u_name, errormsg : ''});
  }
  else{
    u_name = req.user.Username
      res.render('login',{username: u_name, errormsg : ''});
  }

});


app.get('/Dutyfree_linkage',function(req, res){
  var u_name;
  if(req.user == undefined){
      u_name='';
      res.render('Dutyfree_linkage',{username: u_name});
  }
  else{
    u_name = req.user.Username
      res.render('Dutyfree_linkage',{username: u_name});
  }

});

app.get('/password_input',function(req, res){
  var u_name;
  if(req.user == undefined){
      u_name='';
      res.render('password_input',{username: u_name, errormsg : '' });
  }
  else{
    u_name = req.user.Username
      res.render('password_input',{username: u_name, errormsg : ''});
  }

});
app.get('/password_input_error',function(req, res){
  var u_name;
  if(req.user == undefined){
      u_name='';
      res.render('password_input',{username: u_name, errormsg : '아이디와 비밀번호를 확인하세요' });
  }
  else{
    u_name = req.user.Username
      res.render('password_input',{username: u_name, errormsg : '아이디와 비밀번호를 확인하세요'});
  }

});
app.get('/popup_id_check',function(req, res){
      res.render('popup_id_check',{errormsg : ""});
});
app.get('/popup_id_check_error',function(req, res){
      res.render('popup_id_check',{errormsg : "중복된 아이디가 있습니다."});
});


app.get('/User_info_modify',function(req, res){
  var u_name;
  if(req.user == undefined){
      u_name='';
      res.render('User_info_modify',{username: u_name});
  }
  else{
    u_name = req.user.Username
      res.render('User_info_modify',{username: u_name});
  }

});

app.get('/shopping_cart', function(req,res){
  var u_name;
  if(req.user == undefined){
      u_name='';
      res.render('shopping_cart',{username: u_name});
  }
  else{
    u_name = req.user.Username
      res.render('shopping_cart',{username: u_name});
  }

})

//적립금 관리 / 면세점 연동 확인
var reserve = require('./route/check_reserved')();
app.use('/Manage_reserve/', reserve)


app.get('/reserve',function(req,res){
  var u_name;
  if(req.user == undefined){
      u_name='';
      res.render('Manage_reserve',{username: u_name,lt_reserved : req.session.lt_reserved, SL_reserved :req.session.SL_reserved , SSG_reserved : req.session.SSG_reserved})
  }
  else{
    u_name = req.user.Username
    res.render('Manage_reserve',{username: u_name,lt_reserved : req.session.lt_reserved, SL_reserved :req.session.SL_reserved , SSG_reserved : req.session.SSG_reserved})
  }

})



app.get('/popup_lotte',function(req, res){
      res.render('popup_lotte',{errormsg :""});
});

app.get('/popup_shilla',function(req, res){
      res.render('popup_shilla',{errormsg :""});
});

app.get('/popup_shinsegae',function(req, res){
      res.render('popup_shinsegae',{errormsg :""});
});
app.get('/popup_lotte_error',function(req, res){
      res.render('popup_lotte',{errormsg :"아이디 혹은 비밀번호가 다릅니다! 다시 입력하여주세요"});
});

app.get('/popup_shilla_error',function(req, res){
      res.render('popup_shilla',{errormsg :"아이디 혹은 비밀번호가 다릅니다! 다시 입력하여주세요"});
});

app.get('/popup_shinsegae_error',function(req, res){
      res.render('popup_shinsegae',{errormsg :"아이디 혹은 비밀번호가 다릅니다! 다시 입력하여주세요"});
});
app.get('/popup_success',function(req, res){
      res.render('popup_success');
});
//auth 과정
var auth = require('./route/auth_login')(passport);
// '/auth/' 자동으로 가져간다. 고로 auth_login에서는 뒤에있는 login이나 logout같은것만 가져간다.
app.use('/auth/', auth);
