#!/bin/bash
# Takes in a URL, sends a POST request to it, displays the body
curl -s -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
