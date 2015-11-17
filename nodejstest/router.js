function route(handle, pathname, response, postData) {
    // console.log("response in route" + response)
    console.log("Received path name is: " + pathname);
    if (typeof handle[pathname] === 'function') {
        console.log("execute handle function")
        handle[pathname](response, postData);
    } else {
        console.log("There is no corresponding handle function");
        response.writeHead(404, {"Content-type": "text/plain"})
        response.write("Not Found")
        response.end()
    }
}
exports.route = route;
