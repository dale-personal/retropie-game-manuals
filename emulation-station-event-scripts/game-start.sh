#!/usr/bin/env bash

CONSOLE="$1"
ROMNAME=$(basename "$2")

URLENCODED_FILENAME="$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.argv[1].lower()))" "${ROMNAME%.*}")"

URL="http://raspberrypi:8000/$CONSOLE/$URLENCODED_FILENAME/manual"

curl --silent "$URL" >> /dev/null 2>/dev/null &