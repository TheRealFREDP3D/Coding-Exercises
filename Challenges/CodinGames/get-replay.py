"""
------------------------------------------------------------------------------
- Python 3.x.x - get-replay.py                                               -
- Author: Frederick Pellerin                                                 -
- GitHub: https://github.com/TheRealFREDP3D                                  -
- Twitter: https://twitter.com/TheRealFredP3D                                - 
------------------------------------------------------------------------------
- This script uses requests module to make a POST request with the user's    -
- ID and game ID to the CodinGame platform. The response is a JSON containing-
- the replay for the given game. The script then saves the replay in a file  -
- named after the game ID.                                                   -
------------------------------------------------------------------------------
- Usage:                                                                     -
- Change user_ID, game_id and 'rememberMe' cookie and run the script.        -
------------------------------------------------------------------------------
"""

import json
import requests as re

user_ID = 0     # <*****
game_id = 0     # <*****

# Create a persistent session
# The 'rememberMe' cookie is set to authenticate the user. 
with re.Session() as s:
    s.cookies.set('rememberMe', 'CHANGE-ME',       # <*****
                  domain='codingame.com')

    r = s.post(
    'https://www.codingame.com/services/gameResultRemoteService/findByGameId',
    json = [str(game_id), user_ID]
)
    
replay = r.json()

print(replay)

with open(f'{game_id}.json', 'w+') as f:
    f.write(json.dumps(replay))

+-                                                                            -
+-                                                    -
+-                                                                            -
+-                   -
+-                                                                            -
+- The session is used to make a persistent connection to the site, allowing  -
+- the script to reuse the same session across multiple requests.           -
+-                                                                            -
+- The JSON replay is printed to the console and saved in a file.            -
+-                                                                            -
+- The script requires the 'json' and 'requests' modules.                    -
+- The session is automatically closed when the script finishes.   