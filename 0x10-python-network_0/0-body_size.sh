#!/bin/bash
# Displays body size of curl response

curl -s -I $1 | grep  'Content-Length' | sed 's/[^0-9]*//g'
