import requests
with open("dump.html", "wb") as file:
    file.write(requests.get('https://old.reddit.com/').content)
