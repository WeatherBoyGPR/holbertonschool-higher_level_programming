#!/bin/bash
# displays status code
curl -s -o /dev/null -w "%{http_code}\n" $1
