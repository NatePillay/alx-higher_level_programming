#!/bin/bash
#Send a req to URL passed as arg & display status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
