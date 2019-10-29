#!/usr/bin/env python3

print(f'>> logging in')

import os
import praw
import configparser
from time import sleep

PATH = os.path.dirname(os.path.abspath(__file__))

config = configparser.ConfigParser()
config.read(os.path.join(PATH, 'config.ini'))

reddit = praw.Reddit(client_id=config['REDDIT']['ClientId'],
                     client_secret=config['REDDIT']['ClientSecret'],
                     password=config['REDDIT']['Password'], user_agent='genfriends.py',
                     username=config['REDDIT']['Username'])

print('>> reading import.txt')

num_lines = sum(1 for line in open('import.txt'))

with open(os.path.join(PATH,'import.txt')) as f:
	n = 1
	for line in f:
		line = line.rstrip()
		#print(line)
		user = reddit.redditor(line)
		print(f'[{n}/{num_lines}]Found: {user}')
		try:
			user.friend()
			print(f'\t friended')
		except Exception:
			print(f'\t failed')
		n += 1
		sleep(1)

exit()

print('done')
