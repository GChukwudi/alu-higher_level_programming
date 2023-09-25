#!/usr/bin/node
const val = process.argv[2];
if (val === undefined) {
  console.log('No argument');
} else {
  console.log(val);
}
