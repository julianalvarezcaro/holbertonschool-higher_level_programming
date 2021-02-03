#!/usr/bin/node

const nn = process.argv[2];

const n = parseInt(nn);

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (n) {
  console.log(factorial(n));
} else {
  console.log(1);
}
