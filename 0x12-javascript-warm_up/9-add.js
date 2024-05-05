#!/usr/bin/node
// a script that prints the addition of 2 integers
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);
add(first, second);
