#!/bin/bash
#curl command using post here and variables
curl -X POST -d "email:test@gmail.com&subject=I will always be here for PLD" "$1"
