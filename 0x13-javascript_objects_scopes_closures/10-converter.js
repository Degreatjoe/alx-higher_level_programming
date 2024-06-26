#!/usr/bin/node

exports.converter = function (base) {
  return function convert (num) {
    if (num >= base) {
      convert(Math.floor(num / base));
    }
    const remainder = num % base;
    if (remainder >= 10) {
      process.stdout.write(String.fromCharCode(remainder + 87));
    } else {
      process.stdout.write(remainder.toString());
    }
    return '';
  };
};
