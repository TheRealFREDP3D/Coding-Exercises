# ---------------------------------------------------------------------------------------------
# Hash-me-if-you-can.py
# RingZero - Coding Challenges - Hash me if you can
# https://ringzer0team.com/challenges/13
# ---------------------------------------------------------------------------------------------
# Challenge:  
# You have 2 seconds to hash a message located on a web page, using sha512 algorithm
# and send the answer back.
# ---------------------------------------------------------------------------------------------


import requests as re
from bs4 import BeautifulSoup
import hashlib

# 1. Retrieve the HTML content of the web page
url = "http://challenges.ringzer0team.com:10013/"
response = re.get(url)
html_content = response.content

# 2. Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# 3. Find the <div class="message"> element and retrieve its text
message_div = soup.find('div', class_='message')
message_text = message_div.get_text(strip=True)

print(message_text)
print("----------------------------------------------")

# 4. Hash the message using sha512 algorithm and store it in variable solution

message_sha512 = hashlib.sha512(message_text.encode()).hexdigest()

print("SHA512: " + str(message_sha512))
print("----------------------------------------------")

# 5. Send the variable message_sha512 to http://challenges.ringzer0team.com:10013/?r=[solution]

flag = re.post('http://challenges.ringzer0team.com:10013/', data={'r': message_sha512})
print(flag.text)
