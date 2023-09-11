#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg1 = process.argv[2];

const num = parseInt(arg1);

if (!isNaN(num)) {
  const result = factorial(num);
  console.log(result);
}
