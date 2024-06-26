#!/usr/bin/node

function execute (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = { execute };
