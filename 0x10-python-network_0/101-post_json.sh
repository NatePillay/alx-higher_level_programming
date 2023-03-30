#!/bin/bash
#SEND A JSON post request to URL
curl -X POST -H "Content-Type: application/json" -d "@$2" $1
