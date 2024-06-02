# =============================================================================== #
# x-input.py -------------------------------------------------------------------- #
# =============================================================================== #
# Python 3.x.x ------------------------------------------------------------------ #
# Author: CodinGame.com --------------------------------------------------------- #
# GitHub: https://github.com/TheRealFREDP3D ------------------------------------- #
# Twitter: https://twitter.com/TheRealFredP3D ----------------------------------- # 
# =============================================================================== #
# Reference: https://www.codingame.com/ ----------------------------------------- #
# This script reads a replay file in JSON format and extracts the errorstream --- #
# The extracted lines are then written to a new file named 'input.txt'. --------- #
# =============================================================================== #

import json
import os

'''
read the replay from file
'''
with open('replay.json', 'r') as f:
	replay = json.loads(f.read())

stderr = []
for frame in replay['success']['frames']:
    if 'stderr' not in frame.keys(): 
        continue
    
for err in frame['stderr'].split('\n'):
        
# some of the line are marked with '#'to get ignored
    if not err.startswith('#'): 
        stderr.append(err)

'''
write the errorstream to the file 'input.txt'
'''
with open('input.txt', 'w+') as f:
	f.write('\n'.join(stderr))
print('\n'.join(stderr))
