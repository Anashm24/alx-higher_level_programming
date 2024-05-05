#!/usr/bin/node
// a script that prints a square
const count = parseInt(process.argv[2]);
if (count) {
  for (let i = 0; i < count; i++) {
    console.log('X'.repeat(count));
  }
} else {
  console.log('Missing size');
}
