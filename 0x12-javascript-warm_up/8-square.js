#!/usr/bin/node

const n = parseInt(process.argv[2]);

if (!n) {
console.log("Missing size"); }
else {
for (let i = 0; i < n; i++) {
console.log('X'.repeat(n));}
}
