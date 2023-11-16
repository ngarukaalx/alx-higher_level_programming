#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  process.exit(1);
}
const firstFile = process.argv[2];
const secondFile = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(firstFile, 'utf8', (error1, content1) => {
  if (error1) {
    process.exit(1);
  }
  fs.readFile(secondFile, 'utf8', (error2, content2) => {
    if (error2) {
      process.exit(1);
    }
    const concats = content1 + content2;

    fs.writeFile(destinationFile, concats, 'utf8', (erro3) => {
      if (erro3) {
        process.exit(1);
      }
    });
  });
});
