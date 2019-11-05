#!/usr/bin/env python3

import os
import praw
import configparser
import argparse

PATH = os.path.dirname(os.path.abspath(__file__))

config = configparser.ConfigParser()
config.read(os.path.join(PATH, 'config.ini'))

reddit = praw.Reddit(client_id=config['REDDIT']['ClientId'],
                     client_secret=config['REDDIT']['ClientSecret'],
                     password=config['REDDIT']['Password'], user_agent='genfriends.py',
                     username=config['REDDIT']['Username'])

parser = argparse.ArgumentParser(description='reddit username')
parser.add_argument('uname', metavar='spez', type=str,
                    help='reddit username')
parser.add_argument('--dedupe', action='store_true')
args = parser.parse_args()

l = []
if args.dedupe == True:
    for x in reddit.redditor(name=args.uname).submissions.new(limit=None):
        l += [x.url]
    l = list(set(l))
    for x in l:
        print(x)
else:
    for x in reddit.redditor(name=args.uname).submissions.new(limit=None):
        print(x.url)


