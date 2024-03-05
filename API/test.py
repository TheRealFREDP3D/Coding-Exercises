"""Retrieves the challenge ID from the Hack the Box API.

Makes a GET request to the Hack the Box challenges API endpoint, 
parses the HTML response using BeautifulSoup, and extracts the 
challenge ID by finding the 'challenge-meta__title' div.

The challenge ID is printed for debugging purposes.
"""

import requests
from bs4 import BeautifulSoup

url = "https://challenges.hackthebox.eu/api/v1/challenge/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

challenge_id = soup.find("div", {"class": "challenge-meta__title"}).text.strip()

print("Challenge ID:", challenge_id)  # Retrieves the challenge ID from the Hack the Box API response
# and prints it.
