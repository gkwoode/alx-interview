#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  if (!filmData.characters || !Array.isArray(filmData.characters)) {
    console.error('Invalid response from the API');
    process.exit(1);
  }

  // Fetch character names
  const characterUrls = filmData.characters;
  Promise.all(characterUrls.map(url => fetchCharacterName(url)))
    .then(characterNames => {
      console.log('Characters in the movie:');
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error:', error);
      process.exit(1);
    });
});

function fetchCharacterName(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(`Request failed with status code ${response.statusCode}`);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
}

