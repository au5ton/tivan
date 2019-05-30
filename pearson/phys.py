#!/usr/bin/env python3

import subprocess

# http://media.pearsoncmg.com/aw/aw_0media_physics/vts/YF13-VTS/ex01-1.html
# http://media.pearsoncmg.com/aw/aw_0media_physics/vts/YF13-VTS/bp1.html
# http://media.pearsoncmg.com/aw/aw_0media_physics/vts/YF13-VTS/ex44-12.html
# http://media.pearsoncmg.com/aw/aw_0media_physics/vts/YF13-VTS/bp44.html
i = 2

baseurl = "http://media.pearsoncmg.com/aw/aw_0media_physics/vts/YF13-VTS"

# scrape all excercises
for chap in range(1,45):
	for n in range(1,16):
		subprocess.call(f'wget -P data/ {baseurl}/ex{str(chap).zfill(2)}-{n}.html', shell=True)

# scrape all bridging problems
for chap in range(1,45):
	subprocess.call(f'wget -P data/ {baseurl}/bp{chap}.html', shell=True)


exit(0)

subprocess.call(f'echo {str(i).zfill(2)}', shell=True)
