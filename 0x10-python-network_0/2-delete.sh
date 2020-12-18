#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument
# and displays the body of the response
#
# -X excutes requests. I think I could have used that in the previuouds task
curl -s -X DELETE "$1"
