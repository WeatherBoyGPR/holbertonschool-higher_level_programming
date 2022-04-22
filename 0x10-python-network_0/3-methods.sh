#!/bin/bash
# Will display accepted HTTP methods of url inserted
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
