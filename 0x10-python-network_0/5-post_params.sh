#!/bin/bash
#send a POST req command using post here and variables
curl -s -X POST -d "email:test@gmail.com&subject=I will always be here for PLD" "$1"
