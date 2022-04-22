#!/bin/bash
# Will send DELETE request to URL passed as first arg, displays response body
curl -s -X "DELETE" $1
