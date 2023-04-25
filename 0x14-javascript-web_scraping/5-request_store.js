#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const endpoint = process.argv[2];
const filepath = process.argv[3];

request.get(endpoint, (error) => {
	if (error) throw error;
	fs.writeFile(filepath, body, 'utf-8', (error) => {
		if (error) throw error;
	});
});	
