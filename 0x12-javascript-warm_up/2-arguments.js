#!/usr/bin/node

const args = process.argv;

const argsLen = args.length;

let message = '';

if (argsLen === 2) {
  message = 'No argument';
} else if (argsLen === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}
console.log(message);
