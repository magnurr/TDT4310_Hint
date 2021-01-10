import time
import json
maxTime = 1606953600
minTime = 1601683200
results = []

with open('../tweets/users/realDonaldTrump.json') as file:
    ls = json.loads(file.read())
    print(len(ls))
    for obj in ls:
        currentTime = time.strptime(
            obj.get('created_at'), "%a %b %d %H:%M:%S %z %Y")
        EpochTime = int(time.mktime(currentTime))
        if minTime < EpochTime and EpochTime < maxTime:
            results.append(obj)
