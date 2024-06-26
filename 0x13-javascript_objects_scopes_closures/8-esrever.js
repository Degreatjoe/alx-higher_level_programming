#!/usr/bin/node

exports.esrever = function (list) {
  // Determine the length of the list
  const len = list.length;

  // Loop through half of the list
  for (let i = 0; i < Math.floor(len / 2); i++) {
    // Swap elements from start to end
    const temp = list[i];
    list[i] = list[len - 1 - i];
    list[len - 1 - i] = temp;
  }

  // Return the reversed list
  return list;
};
