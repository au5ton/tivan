#!/usr/bin/env python3

import os
import subprocess
import argparse
from urllib.parse import urlparse

parser = argparse.ArgumentParser(description='some url')
parser.add_argument('url', metavar='https://google.com', type=str,
                    help='some url')
parser.add_argument('--out', type=str)
args = parser.parse_args()

url = urlparse(args.url)

if url.netloc == 'imgur.com':
	print('[download.py] imgur.com')
	subprocess.run(f'java -jar ripme.jar --l {args.out} --u {args.url}', shell=True)
elif url.netloc == 'i.imgur.com':
	print('[download.py] i.imgur.com')
	subprocess.run(f'wget -P {args.out} --no-clobber {args.url}', shell=True)
elif url.netloc == 'youtube.com':
	print(f'[download.py] youtube.com: skipping {args.url}')
else:
	print(f'[download.py] generic: {args.url}')
	subprocess.run(f'youtube-dl -o \"{args.out}/%(title)s-%(id)s.%(ext)s\" {args.url}', shell=True)

# http://imgur.com/a/KQVGOpS


