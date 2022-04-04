#!/usr/bin/node

exports.callMeMoby = (x, theFunction) => {
  for (; x > 0; x--) {
    theFunction();
  }
};
