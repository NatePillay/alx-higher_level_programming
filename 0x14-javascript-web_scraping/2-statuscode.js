#!/usr/bin/node
const request = require('require');

const url = process.argv[2];
request(url, (err, res, body) => {
	if (!err) console.log('code:', res.statusCode);
});
