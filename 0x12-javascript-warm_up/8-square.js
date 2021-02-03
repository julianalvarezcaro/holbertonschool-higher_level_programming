#!/usr/bin/node

const size = process.argv[2];

if (parseInt(size)) {
  let w;
  let h;
  for (h = 0; h < size; h++) {
    for (w = 0; w < size; w++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
