#!/bin/bash
cd "$(dirname "$0")"
#exit

# https://github.com/aliparlakci/bulk-downloader-for-reddit
# python3 ~/bdfr2/script.py --directory ./data --user $1 --submitted --quit

# https://github.com/RipMeApp/ripme
ORANGE='\033[0;35m'
BOLD='\e[1m'
NC='\033[0m' # No Color

echo -e "\n${ORANGE}${BOLD}/u/${1}${NC}"
# exit
#java -jar ./ripme.jar --ripsdirectory "$OUT_DIR" --url "https://old.reddit.com/user/"$1 -t 2
# use rename -n for dryrun, -f for force
# truncate to 150 characters (not including extension)
# https://unix.stackexchange.com/a/33061
#find "$OUT_DIR" -exec rename -f 's/^(.{150}).*(\..*)$/$1$2/' {} \;

mkdir -p "./dips2/$1"

#./gensubmissions.py "$1" | parallel -j 4 youtube-dl -o "'./dips2/$1/%(title)s-%(id)s.%(ext)s'" {}

./gensubmissions.py "$1" | parallel -j 4 ./download.py --out "./dips2/$1" {}
