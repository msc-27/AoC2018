#/bin/sh
sort day4 | gawk '/#/ {match($0,"#[0-9]*",m);print m[0]} !/#/ {print(substr($0,16,2))}' > day4b
