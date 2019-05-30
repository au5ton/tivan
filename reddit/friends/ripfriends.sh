#!/bin/bash
cd "$(dirname "$0")"

while read p; do
	./ripuser.sh "$p"
done <friends.txt
