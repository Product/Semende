
var fs = require('fs');
var parse = require('csv-parse')
var async = require('async');


var eventlist = [];
function getdata(dutyfree){
      var inputFile='./timesale/'+dutyfree+'.csv';
      var parser = parse({delimiter: ','}, function (err, data) {
        async.eachSeries(data, function (line, callback_list) {
          // do something with the line

          eventlist.push(line);
          callback_list();
          // doSomething(line).then(function() {
          //   // when processing finishes invoke the callback to move to the next one
          //   callback();
          // });
        });
        // console.log(eventlist);
        callback(eventlist);
      });
      fs.createReadStream(inputFile).pipe(parser);
}
getdata("lottePoint");
