#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');

request(url, function (error, response, body) {
  error = 0;
  fs.writeFile(file, body, error => {
    if (error) {
      console.log(error);
    }
  });
});
