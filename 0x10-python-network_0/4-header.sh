#!/bin/bash
# Takes in a URL, sends a GET request to it, displays the body
curl -s -G -H "X-HolbertonSchool-User-Id: 98" "$1"
