#!/bin/bash
#script to takes in URL and displays all HTTP methods server accepts
curl -sI "$1" | grep "Allow" |cut -d " " -f 2-
