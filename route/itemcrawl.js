var PythonShell = require('python-shell');
var async = require('async');

//보여주기용
var itemlist ={
  [
    {
      itemname : "ULTRA FACIAL TONER",
      price : { SSG : [20,0] , SL : [20, 0] , LT : [20, 0] }
    },
    {
      itemname : "제니피끄 유쓰 액티베이터 아이 컨센트레이트 듀오 20ml*2",
      price : { SSG : [142,0] , SL : [142, 0] , LT : [142, 0] }
    },
    {
      itemname : "Atoderm Stick Levres",
      price : { SSG : [11,0] , SL : [11, 9.90] , LT : [11, 9.90] }
    },
    {
      itemname : "자음 2종",
      price : { SSG : [91,0] , SL : [91, 86.45] , LT : [91, 86.45] }
    },
    {
      itemname : "레네르지 멀티 리프트 리디파이닝 뷰티 로션 200ml",
      price : { SSG : [0,0] , SL : [49, 0] , LT : [49, 0] }
    },
    {
      itemname : "하이드라비오 에센스 로션(수분 미백 부스터)",
      price : { SSG : [23,0] , SL : [23, 20.70] , LT : [23, 20.70] }
    },
    {
      itemname : "어드밴스드 나이트 리페어 아이 컨센트레이트 매트릭스 듀오",
      price : { SSG : [135,0] , SL : [135, 0] , LT : [135, 0] }
    },
    {
      itemname : "더 트루 크림 아쿠아밤 125ml",
      price : { SSG : [62,0] , SL : [62, 0] , LT : [62, 0] }
    }
  ]
}


const UTIL = (function(){

  function getIteminfo(itemname, callback_info){
    var itemprice = []
    async.map(item_list, function(item ,callback){
      if(item.itemname==itemname){
        itemprice.push(item.price);
      }
    },
    function(err,result){
      if(err) console.log(err);
        //list 받아오기 완료
        else {
          console.log('Finish the File list');
          callback_info(itemprice);
        }
      }
    )
    // async.parallel([
    //   function(callback){
    //
    //     PythonShell.run('./python/reserveDutyfree/getLotte.py', item, function (err, price) {
    //       if (err) throw err;
    //       itemprice.push(price);
    //       callback(null,"finish");
    //     });
    //     else callback(null,'null');
    //   },
    //   function(callback){
    //
    //     PythonShell.run('./python/reserveDutyfree/getShinla.py', item, function (err, price) {
    //       if (err) throw err;
    //       itemprice.push(price);
    //       callback(null,"finish");
    //     });
    //   else callback(null,'null');
    //   },
    //   function(callback){
    //
    //     PythonShell.run('./python/reserveDutyfree/getSSG.py', item, function (err, price) {
    //       if (err) throw err;
    //       itemprice.push(price);
    //       callback(null,"finish");
    //     });
    //     else callback(null,'null');
    //   }
    //
    // ],function(err,result){
    //   callback_info(itemprice);
    // })
  }

  return {
      getIteminfo : getIteminfo
  }
})();

module.exports = UTIL;
