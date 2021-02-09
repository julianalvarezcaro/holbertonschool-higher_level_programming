#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ocur = 0;
  for (element of list) {
    if (element === searchElement) {
      ocur++;
    }
  }
  return ocur;
};
