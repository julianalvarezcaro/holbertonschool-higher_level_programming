#!/usr/bin/node

function compareFunc (a, b) {
  if (a > b) {
    return -1;
  }
  if (a < b) {
    return 1;
  }
  return 0;
}

const args = process.argv;
if (args.length <= 3) {
  console.log(1);
} else {
  const secondBig = args.sort(compareFunc)[1];
  console.log(secondBig);
}
