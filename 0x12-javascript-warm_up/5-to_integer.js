#!/usr/bin/node
// print an integer if the first argument can be converted to an integer
const num = parseInt(process.argv[2]);
if (num) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
