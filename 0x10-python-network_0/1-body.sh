#!/bin/bash
# Takes in a URL, sends a GET request to the URL
curl -s -L -G "$1"
