//write a script that prints a size of square 
// if the first argumant cant be converted to an integer print missing size 
// yo must use the charcter x to print the square 


for (let i = 0; i < process.argv[2]; i++) {
  console.log('X'.repeat(process.argv[2]));
}