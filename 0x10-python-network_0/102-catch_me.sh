#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -s "0.0.0.0:5000/catch_me" -H "Origin: You got me!"
