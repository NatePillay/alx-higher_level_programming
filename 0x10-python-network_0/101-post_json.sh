#!/bin/bash
#SEND A JSON post request to URL
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
