#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2]; // Get file path from command-line argument

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
  } else {
    console.log('File content:', data);
  }
});

