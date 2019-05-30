#!/bin/bash
cd "$(dirname "$0")"

# https://github.com/aliparlakci/bulk-downloader-for-reddit

python3 ~/bdfr2/script.py --directory ./data --user $1 --submitted --quit
