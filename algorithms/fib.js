//create a function  where a third number is the sum of the preceding two numbers
//and returns the tenth number in the sequence
function fib(){
//within the defined function, create a variable that will hold the first two
//integer holding variables
  var a = 0;
  var b = 1;
//create a third variable that is the sum of the first two variables
  var c = a + b;
//use a for loop that runs ten times
  for(var i = 0; i < 10; i++){
//we'll need to have the first two variables displayed and, following that, the 
    console.log(a);
    // console.log(b);
//sum of those two variables
    a + b;
//the third variable (c) equals the sum of the first variable (a) plus the second
//variable (b)
    c = a + b;
//a will now hold the value of b 
    a = b;
//b will now hold the value of c
    b = c;
//for loop ends
  }
//return a
  return a;
}
// call function
console.log(fib());