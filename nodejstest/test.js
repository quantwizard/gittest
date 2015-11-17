console.log("argv:", process.argv)
console.log("argc:", process.argc)
console.log(process.env.PORT||3000)

function say(word){
  console.log(word);
}

function execute(someFunction, value){
  someFunction(value);
}

execute(say,"Hello");
