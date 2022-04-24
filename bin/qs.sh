#!/bin/bash

WINE="/opt/homebrew/bin/wine64"
QUARTUS_PATH="$HOME/quartus"

REQ_PROGRAM="`basename $0`"
PROGRAM="$QUARTUS_PATH/bin64/$REQ_PROGRAM"

WINEDEBUG="-all" exec $WINE "$PROGRAM" "$@"
