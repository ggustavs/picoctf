#!/bin/bash
exiftool cat.jpg | grep License | cut -d ":" -f 2 | cut -d " " -f 2 | base64 --decode
echo
echo "done"
