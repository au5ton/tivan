#!/bin/bash
cd "$(dirname "$0")"

#while read p; do
#	./ripuser.sh "$p"
#done <friends.txt

cat friends.txt | parallel -j 2 ./ripuser.sh {}
