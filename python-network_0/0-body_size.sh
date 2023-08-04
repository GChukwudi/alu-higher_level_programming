#!/bin/bash
# getting content and displaying just content lenght information 
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f 2
