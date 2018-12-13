#!/bin/sh
cut -c 2- day3 | sed 's/[^0-9][^0-9]*/,/g' > day3b
