#!/usr/bin/node

function factorial (n) {
  // Base case: factorial of 0 is 1
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    // Recursive case: factorial of n is n * factorial(n-1)
    return n * factorial(n - 1);
  }
}

const args = process.argv.slice(2);
const num = parseInt(args[0]);

console.log(factorial(num));
