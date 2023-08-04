#!/bin/bash
# displays http methods
curl -sI "$1" -X OPTIONS | grep "Allow" | cut -c 8-
