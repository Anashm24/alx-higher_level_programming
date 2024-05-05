#!/usr/bin/node
// a script that prints the first argument passed to it
const arg1 = process.argv[2];
if (arg1) {
  console.log(arg1);
} else {
  console.log('No argument');
}
