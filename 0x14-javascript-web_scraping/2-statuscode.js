#!/usr/bin/node
const request = require('require');

const url = process.argv[2];
request(endpoint, (err, res, body) => {
	if (!err) console.log('code:',res.statusCode);
});
