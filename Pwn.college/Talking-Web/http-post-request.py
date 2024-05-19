# -----------------------------------------------------------------------------
# Python program to make an HTTP request with JSON data
# -----------------------------------------------------------------------------

import requests as re

url = 'http://127.0.0.1'
headers = {'Content-Type': 'application/json'}
data = {'a': 'ce3ffc48eecfc9e0a7ccb8918e723392', 'b': '27ab104f ff5e2dce&533584b5#6330da2a'}

response = re.post(url , data=data )
print(response.text)
print(f'Status code: {response.status_code}')

print(f'Response body: {re.json()}')
