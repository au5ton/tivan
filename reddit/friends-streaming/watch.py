#!/usr/bin/env python3

import os
import os.path
import subprocess
import praw
import argparse
import configparser
import time
from colorama import init
init()
from colorama import Fore, Back, Style

from prawcore.exceptions import PrawcoreException
import praw.exceptions

PATH = os.path.dirname(os.path.abspath(__file__))
FOLDER = None

config = configparser.ConfigParser()
config.read(os.path.join(PATH, 'config.ini'))

parser = argparse.ArgumentParser(description='streaming api')
parser.add_argument('folder', metavar='rips', type=str,
                    help='folder name')
args = parser.parse_args()

print(f'>> logging in')
reddit = praw.Reddit(client_id=config['REDDIT']['ClientId'],
                     client_secret=config['REDDIT']['ClientSecret'],
                     password=config['REDDIT']['Password'], user_agent='genfriends.py',
                     username=config['REDDIT']['Username'])

# friends = reddit.user.friends()
# print(f'>> friends pulled ({len(friends)})')
# usernames = [u.name for u in friends]
# usernames.sort(key=str.lower)

# exit()

# print('>> writing friends.txt')
# with open(os.path.join(PATH,'friends.txt'), 'w') as f:
#     for u in usernames:
#         f.write(f'{u}\n')
#         print('.', end='')
#     f.close()
# print('done')

if os.path.isabs(args.folder):
    FOLDER = args.folder
else:
    FOLDER = os.path.join(PATH, args.folder)

if not os.path.isdir(FOLDER):
    os.mkdir(FOLDER)



running = True
while running:
    try:
        for submission in reddit.subreddit('friends').stream.submissions():
            print(f'{Fore.CYAN}Downloading https://redd.it/{submission.id} (/u/{submission.author.name}){Style.RESET_ALL}')
            if not os.path.isdir(os.path.join(FOLDER, submission.author.name)):
                os.mkdir(os.path.join(FOLDER, submission.author.name))
            subprocess.run(f'./download.py {submission.url} --out {os.path.join(FOLDER, submission.author.name)}', shell=True)
    except KeyboardInterrupt:
        print(f'Termination received. Goodbye!')
        running = False
    except PrawcoreException:
        print(f'run loop')
        time.sleep(10)

