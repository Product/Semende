var request = require("request");
var url = "http://kor.lottedfs.com/kr/product/productDetail?prdNo=10001860657&dispShopNo1=1100001&dispShopNo2=1100002&dispShopNo3=1100003";
var cheerio = require("cheerio");
request(url, function(error, response, body) {
  if (error) throw error;
  console.log(body);
  var $ = cheerio.load(body);
  var postElements = $("div.priceArea");
  postElements.each(function() {
  var postTitle = $(this).find("strong").text();
  console.log(postTitle);
  });

});
