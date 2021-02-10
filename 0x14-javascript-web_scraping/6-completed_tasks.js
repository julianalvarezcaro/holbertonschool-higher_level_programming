#!/usr/bin/node

const request = require('request');
const url = process.argv[2] + '?completed=true';

request(url, function (error, response, body) {
  error = 0;
  const jsonRep = JSON.parse(body);
  const dict = {};
  let prevUser = -1;
  for (const todo of jsonRep) {
    const user = todo.userId;
    if (user !== prevUser) {
      prevUser = user;
      dict[user] = 0;
    }
    dict[user] += 1;
  }
  console.log(dict);
});
