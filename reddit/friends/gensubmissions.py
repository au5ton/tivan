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
args = parser.parse_args()

for x in reddit.redditor(name=args.uname).submissions.new(limit=None):
	print(x.url)


