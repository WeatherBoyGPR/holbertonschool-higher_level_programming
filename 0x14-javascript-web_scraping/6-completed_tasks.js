#!/usr/bin/node
/* Will compute and print number of completed tasks, sorted by id
 * arg1 - API URL
 */

const Request = require('request');

if (process.argv.length < 3) {
  console.log('invalid number of args');
} else {
  Request(process.argv[2], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const list = JSON.parse(body);
    const res = {};

    if (list.length > 0) {
      for (const i in list) {
        if (res[String(list[i].userId)] === undefined && list[i].completed === true) {
          res[String(list[i].userId)] = 0;
        }
      }
      for (const i in list) {
        if (res[String(list[i].userId)] !== undefined && (list[i]).completed === true) {
          res[String(list[i].userId)] += 1;
        }
      }
    }
    console.log(res);
  });
}
