#!/bin/bash
# WIll take in url, send post request
curl -s -X "POST" -d "email=test@gmail.com&subject=I will always be here for PLD" $1
