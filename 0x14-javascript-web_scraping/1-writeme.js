#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const stringWrite = process.argv[3];

fs.writeFile(filePath, stringWrite, 'utf-8', (err) => {
	if (err) throw err;
});	
