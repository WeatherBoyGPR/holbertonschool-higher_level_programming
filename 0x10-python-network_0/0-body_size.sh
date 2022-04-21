#!/bin/bash
# Displays body size of curl response

curl -s $1 | wc -c
