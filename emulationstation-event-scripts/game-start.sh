#!/usr/bin/env bash

DIRNAME=$(dirname "$1")
CONSOLE=$(basename "$DIRNAME")
ROMNAME="$2"
ROM=$(basename "$1")

SCUMMVM='launch.scummvm'

if [[ $ROM == $SCUMMVM ]]
then
  ROMNAME="$CONSOLE"
  CONSOLE="scummvm"
fi

URLENCODED_FILENAME="$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.argv[1]))" "${ROMNAME}")"

URL="http://raspberrypi.local:8000/$CONSOLE/$URLENCODED_FILENAME/manual"

curl --silent "$URL" >> /dev/null 2>/dev/null