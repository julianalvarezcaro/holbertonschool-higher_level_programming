#!/usr/bin/node

exports.esrever = function (list) {
  const lastIndex = list.length - 1;
  let index;
  const reversed = [];

  for (index = lastIndex; index >= 0; index--) {
    reversed.push(list[index]);
  }
  return reversed;
};
