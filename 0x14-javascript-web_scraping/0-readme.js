#!/usr/bin/node

const arg = process.argv[2];
const fs = require('fs');

fs.readFile(arg, (error, data) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(data.toString());
});
