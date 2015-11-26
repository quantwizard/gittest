console.log("argv:", process.argv)
console.log("argc:", process.argc)
// process.env.PORT = 8000
console.log(process.env)

function say(word){
  console.log(word);
}

function execute(someFunction, value){
  someFunction(value);
}

execute(say,"Hello");
