#!/usr/bin/node
const request = require('request');
const value = process.argv[2]
const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + value 

request(endpoint, (error, response, body) => {
	if (error) throw error;
	console.log(JSON.parse(body).title);
});
