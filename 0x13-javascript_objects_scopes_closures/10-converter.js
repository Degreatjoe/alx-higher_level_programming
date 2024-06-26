#!/usr/bin/node

exports.converter = function (base) {
  function convert (num) {
    if (num >= base) {
      convert(Math.floor(num / base));
    }
    process.stdout.write(num.toString());
    if (num !== 10) {
      process.stdout.write('\n');
    }
  }
  return convert;
};
