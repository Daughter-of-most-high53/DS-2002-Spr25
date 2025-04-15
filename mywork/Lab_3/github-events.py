#!/opt/homebrew/bin/python3

import os
import json
import requests

GHUSER = os.getenv('Daughter-of-the-mosthigh53')

url = 'https://github.com/Daughter-of-most-high53/DS-2002-Spr25'.format(GHUSER)

r = json.loads(requests.get(url).text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)



