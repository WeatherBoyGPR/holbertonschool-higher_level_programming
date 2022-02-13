#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length - 1;

  let buf;
  for (let i = 0; i < (len / 2); i++) {
    buf = list[i];
    list[i] = list[len - i];
    list[len - i] = buf;
  }

  return (list);
};
