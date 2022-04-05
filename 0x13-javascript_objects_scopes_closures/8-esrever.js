#!/usr/bin/node
// contains esrever function

/*
 * esrever - reverses list
 * @list: list to reverse
 *
 * Return: reversed list
 */
exports.esrever = function (list) {
  const res = list.slice();
  for (let i = 0, j = (res.length - 1); i < j; i++, j--) {
    [res[i], res[j]] = [res[j], res[i]];
  }
  return (res);
};
