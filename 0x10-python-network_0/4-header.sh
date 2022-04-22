#!/bin/bash
# Will send GET request to URL passed as first arg, displays response body
curl -sH "X-School-User-Id:98" "$1"
