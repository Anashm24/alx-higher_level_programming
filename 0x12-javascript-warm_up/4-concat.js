#!/usr/bin/node
// a script that prints two arguments passed to it, in the following format: “ is ”
const first = process.argv[2];
const second = process.argv[3];
if (first && second) {
  console.log(`${first} is ${second}`);
} else if (first) {
  console.log(`${first} is undefined`);
} else {
  console.log('undefined is undefined');
}
