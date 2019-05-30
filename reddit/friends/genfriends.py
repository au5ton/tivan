#!/usr/bin/env python3

print(f'>> logging in')

import os
import praw
import configparser

PATH = os.path.dirname(os.path.abspath(__file__))

config = configparser.ConfigParser()
config.read(os.path.join(PATH, 'config.ini'))

reddit = praw.Reddit(client_id=config['REDDIT']['ClientId'],
                     client_secret=config['REDDIT']['ClientSecret'],
                     password=config['REDDIT']['Password'], user_agent='genfriends.py',
                     username=config['REDDIT']['Username'])

friends = reddit.user.friends()
print(f'>> friends pulled ({len(friends)})')
usernames = [u.name for u in friends]
usernames.sort()

print('>> writing friends.txt')
with open(os.path.join(PATH,'friends.txt'), 'w') as f:
	for u in usernames:
		f.write(f'{u}\n')
		print('.', end='')
	f.close()
print('done')
