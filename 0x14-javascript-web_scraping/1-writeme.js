#!/usr/bin/node
// script that writes a string to a file.

const fs = require("fs");
const filePath = process.argv[2];
const writeData = process.argv[3];

fs.writeFile(filePath, writeData, "utf-8", (error) => {
  if (error) {
    console.log(error);
  }
});
