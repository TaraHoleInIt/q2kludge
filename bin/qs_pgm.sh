#!/bin/bash

PGM_FILE=`echo "$@" | grep -Eo "[A-Za-z\.0-9\_\-\s]*$"`
TEMP_FILE=".`basename $PGM_FILE`.svf"

quartus_cpf -c -q 10MHz -g 3.3 -n p "$PGM_FILE" "$TEMP_FILE"
openocd -f interface/altera-usb-blaster.cfg -c "jtag newtap ep2c20 tap -expected-id 0x20B30DD -irlen 10" -c "init" -c "scan_chain" -c "svf $TEMP_FILE" -c "exit"
rm "$TEMP_FILE"
