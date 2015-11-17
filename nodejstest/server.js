
http = require("http")
url = require("url")
qs = require("querystring")

function start(route, handle){
    http.createServer(function(request, response){
        console.log("request is received")
        var pathname = url.parse(request.url).pathname
        console.log("pathname is:" + pathname)
        request.setEncoding("utf8");
        postData = ""
        // request.addListener("data", function(postDataChunk){
        //     postData += postDataChunk;
        request.on("data", function(postDataChunk){
            postData += postDataChunk;

            // console.log("current data is: " + postData);
            console.log("Received POST data chunk '"+
      postDataChunk + "'.");

        });
        request.addListener("end", function(){
            console.log("in end, postdata is: '" + postData +"'.")
            route(handle, pathname, response, postData)
        })
        // console.log("response in server" + response)
        
        // response.writeHead(404, {"Content-type": "text/plain"})
        // response.write("Not Found")
        // response.end()
        // queryUrl = url.parse(request.url).query
        // console.log("query value is:" + qs.parse(queryUrl)['query'])
        
    }).listen(8888)
    console.log("Server is started")
}
exports.start = start