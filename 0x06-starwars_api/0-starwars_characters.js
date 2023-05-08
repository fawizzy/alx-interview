#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const output = JSON.parse(body);
    const characters = output.characters;
    // console.log(characters)
    character(characters, 0);
  } else {
    console.log('error fetching data');
  }
});

function character (characters, n) {
  request(characters[n], (error, response, body) => {
    if (!error) {
      const names = JSON.parse(body);
      console.log(names.name);
      if (n + 1 < characters.length) {
        character(characters, n + 1);
      }
    } else {
      console.log('error fetching character name');
    }
  });
}
