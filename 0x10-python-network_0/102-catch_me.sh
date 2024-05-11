#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!

# Send a POST request with the data specified
curl -s -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
