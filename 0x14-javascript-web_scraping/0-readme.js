#!/usr/bin/node

const args = process.argv;
const fs = require('fs');

fs.readFile(`./${args[2]}`, (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data.toString());
});
