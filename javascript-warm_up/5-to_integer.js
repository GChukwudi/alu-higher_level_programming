#!/usr/bin/node
const numb = Math.floor(Number(process.argv[2]));
console.log(isNaN(numb) ? 'Not a number' : `My number: ${numb}`);
