#!/usr/bin/env bash

curl -I $1 | grep "Content-Length" | sed "s/[^0-9]*//g"
