var http = require('http');
var fs = require('fs');

var server = http.createServer(function(req, res) {
    console.log("request arrived");

    // fs.readFile(__dirname + '/data.txt', function(err, data){
    //     res.end(data);
    // });

    var stream = fs.createReadStream(__dirname + '/data.txt');
    stream.pipe(res);
});

server.listen(8000);