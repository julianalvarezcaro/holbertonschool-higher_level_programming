#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const jsonRep = JSON.parse(body);
  const dict = {};
  for (const todo of jsonRep) {
    const user = todo.userId;
    if (todo.completed) {
      if (dict[user]) {
        dict[user]++;
      } else {
        dict[user] = 1;
      }
    }
  }
  console.log(dict);
});
