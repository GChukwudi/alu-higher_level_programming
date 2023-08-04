#!/bin/bash
# sends a json post request to a rul passsed as the first argument,a dn displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
