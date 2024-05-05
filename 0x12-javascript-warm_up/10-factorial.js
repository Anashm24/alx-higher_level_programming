#!/usr/bin/node
// a script that computes and prints a factorial
function factorial (first) {
  if (first <= 1) {
    return 1;
  }
  return first * factorial(first - 1);
}
const num = parseInt(process.argv[2]);
console.log(factorial(num));
