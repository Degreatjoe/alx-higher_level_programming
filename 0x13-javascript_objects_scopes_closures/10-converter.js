#!/usr/bin/node

exports.converter = function (base) {
  function convert (num) {
    if (num >= base) {
      convert(Math.floor(num / base));
    }
    process.stdout.write(num % base.toString(10));
  }
  return convert;
};
