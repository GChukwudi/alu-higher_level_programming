#!/bin/bash
# send a request to a url passed as an argument,and displays only the status code of the response
curl -so /dev/null --write-out "%{http_code}" "$1"
