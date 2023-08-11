#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

const getCharacters = async (movieId) => {
  const url = baseUrl + movieId;
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        try {
          const data = JSON.parse(body);
          resolve(data.characters.map((character) => {
            const characterId = character.split('/').slice(-2, -1)[0];
            return `https://swapi-api.alx-tools.com/api/people/${characterId}/`;
          }));
        } catch (parseError) {
          reject(parseError);
        }
      }
    });
  });
};

const main = async () => {
  try {
    const characters = await getCharacters(movieId);
    for (const character of characters) {
      request.get(character, (error, response, body) => {
	if (!error) {
	  const characterData = JSON.parse(body);
          console.log(characterData.name);
	}
      }
    )}
  } catch (error) {
    console.error('Error:', error.message);
  }
};

main();
