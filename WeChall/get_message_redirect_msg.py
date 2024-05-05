import requests

url = "https://www.wechall.net/challenge/training/programming1/index.php?action=request"
header = "WC=21825277-65452-vb8rQC4JRStGXiYI"

message = requests.get(url, headers={"Cookie": header}).text
print(message)1/index.php?answer="


solve-url = "https://www.wechall.net/challenge/training/programming"
solve = request.get(solve-url + message)

print(solve.text())