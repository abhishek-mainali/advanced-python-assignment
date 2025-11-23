#!/bin/sh
set -e
gcc -shared -fPIC -o libstringlib.so stringlib.c
echo "Built libstringlib.so"
