#!/usr/bin/node

const args = process.argv.slice(2);

const integers = args.map((arg) => parseInt(arg));

const validIntegers = integers.filter((num) => !isNaN(num));

if (validIntegers.length < 2) {
  console.log(0);
} else {
  let largest = validIntegers[0];
  let secondLargest = validIntegers[1];

  for (let i = 2; i < validIntegers.length; i++) {
    if (validIntegers[i] > largest) {
      secondLargest = largest;
      largest = validIntegers[i];
    } else if (
      validIntegers[i] > secondLargest &&
      validIntegers[i] !== largest
    ) {
      secondLargest = validIntegers[i];
    }
  }

  console.log(secondLargest);
}
