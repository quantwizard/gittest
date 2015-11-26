function onTimeout(name){
    console.log("timeout event "+name+" is triggered");
}

function onInterval(name){
    console.log("interval event "+ name+" is triggered.");
}

timeoutId = setTimeout(onTimeout, 1000, "aaa");
intervalId = setInterval(onInterval, 3000, "bbbb");
setTimeout(function(){
    console.log("clear interval now...");
    clearInterval(intervalId);
}, 10000);