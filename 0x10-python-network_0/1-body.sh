#!/bin/bash
# Takes in a URL, sends a GET request to the URL
curl -s -L -G "$1"
# INITIALY I TRIED: curl -G "0.0.0.0:5000/route_1"
# But it says that the page has a redirection, so I had to follow that
