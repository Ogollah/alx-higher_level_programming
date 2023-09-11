#!/usr/bin/node

const args = process.argv.slice(2);

const updatedIntegers = args.map((arg) => {
  const num = parseInt(arg);
  return num === 12 ? 89 : num;
});

console.log(updatedIntegers.join(' '));
