#!/usr/bin/env bash

curl -I -s $1 | grep "Content-Length" | sed "s/[^0-9]*//g"
