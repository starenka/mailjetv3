
var fs = require ('fs');
var mailjet = require ('./mailjet-apiv3-nodejs/').connect(process.env['MJ_APIKEY_PUBLIC'], process.env['MJ_APIKEY_PRIVATE']);

var file = fs.readFileSync('./test.csv');
// var call = mailjet.post('contactslist').id(38).action('CSVData')
var call = mailjet.post('contactslist')
      .id(38)
	      .action('csvdata/text:plain');


var res = call.request(file);

res.on('error', function (error, response) {
	console.log (error);
});

res.on('success', function (response, body) {
	console.log (response.statusCode, body)
});
