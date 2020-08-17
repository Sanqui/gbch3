#!/bin/bash
f=$(basename "$1" .gbs)
/home/sanqui/romhacking/gb/tools/gbsplay/gbsplay -g 0 -f 0 -t 180 -o stats "$1" > "data/$f.txt"
