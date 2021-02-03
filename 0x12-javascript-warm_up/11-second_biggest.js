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

const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(1);
} else {
  const secondBig = args.sort(compareFunc)[1];
  console.log(secondBig);
}
