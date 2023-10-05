#!/usr/bin/node
const request = require('request');
const { argv, exit } = require('process');

if (argv.length !== 3) {
  exit(0);
}

const options = {
  url: `https://swapi-api.hbtn.io/api/films/${argv[2]}/`,
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8'
  }
};
