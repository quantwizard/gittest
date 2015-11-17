fs = require("fs")


function starts(response, postData) {
    console.log("this is start function");
    var body = '<html>'+
    '<head>'+
    '<meta http-equiv="Content-Type" content="text/html; '+
    'charset=UTF-8" />'+
    '</head>'+
    '<body>'+
    '<form action="/upload" method="post">'+
    '<textarea name="text" rows="20" cols="60"></textarea>'+
    '<input type="submit" value="Submit text" />'+
    '</form>'+
    '</body>'+
    '</html>';

    response.writeHead(200, {"Content-Type": "text/html"});
    response.write(body);
    response.end();

}

function upload(response, postData) {
    console.log("this is upload function");
    response.writeHead(200, {"Content-type": "text/plain"})
    response.write("You've sent:"+postData)
    response.end();
}

function show(response, postData) {
  console.log("Request handler 'show' was called.");
  fs.readFile("/Users/eliu/Downloads/modelx.jpg", "binary", function(error, file) {
    if(error) {
      response.writeHead(500, {"Content-Type": "text/plain"});
      response.write(error + "\n");
      response.end();
    } else {
      response.writeHead(200, {"Content-Type": "image/png"});
      response.write(file, "binary");
      response.end();
    }
  });
}

exports.starts = starts;
exports.upload = upload;
exports.show = show;