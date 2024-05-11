#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument and displays the body of the response
# It sends the contents of a file, passed with the filename as the second argument of the script, in the body of the request

# Check if the file exists and is readable
if [ ! -r "$2" ]; then
    echo "File '$2' does not exist or is not readable"
    exit 1
fi

# Check if the file contains valid JSON
if ! jq -e . >/dev/null 2>&1 <"$2"; then
    echo "Not a valid JSON"
    exit 1
fi

# Send POST request with JSON file as body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
