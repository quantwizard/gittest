var server = require("./server")
var router = require("./router")
var handler = require("./requestHandlers")
var handle = {}
handle["/start"] = handler.starts
handle["/"] = handler.starts
handle['/upload'] = handler.upload
handle['/show'] = handler.show
server.start(router.route, handle)