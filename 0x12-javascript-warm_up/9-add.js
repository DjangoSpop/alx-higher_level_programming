//write a script that prints adition of two integer 
// the first argument is the first integer 
//secound argument is the second 
//you must use console.log
//you are not allowed to use var 


function add(a,b){
    return a+b;
}
console.log(add(parseInt(process.argv[2]),parseInt(process.argv[3])));