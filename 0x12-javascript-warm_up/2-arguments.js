#!/usr/bin/node
/**
 * prints a message depending of the number of arguments passed
 * if no argument passed it print No argument
 */
const NumArgs = process.argv.length - 2;
if (NumArgs === 0) {
  console.log('No argument');
} else if (NumArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
