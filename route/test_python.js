var PythonShell = require('python-shell');

var options={
  mode: 'text',

 pythonPath: '',

 pythonOptions: ['-u'],

 scriptPath: '',

 args: ['john6939','whdlrghks1!']
}

//Lotte Auth

PythonShell.run('../python/authDutyfree/checkShinsaegaeID.py', options, function (err, results) {

  if (err) throw err;

  // if(results)
  console.log(results);

});


//Shinsaegae


// PythonShell.run('./python/authDutyfree/checkShinsaegaeID.py', options, function (err, results) {
//
//   if (err) throw err;
//
//   // if(results)
// //   console.log(results);
// //
// // });
//
//
//
// PythonShell.run('./python/authDutyfree/checkShinlaID.py', options, function (err, results) {
//
//   if (err) throw err;
//
//   // if(results)
//   console.log(results);
//
// });
