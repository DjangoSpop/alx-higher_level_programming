const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: node writeToFile.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
  } else {
    console.log(`Content has been successfully written to ${filePath}`);
  }
});

