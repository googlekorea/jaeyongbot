# -*- coding: utf-8 -*-
from config.webhookurl import webhookurl
import requests
import json
import sys

json_data = open('/home/cse20111635/jaeyongbot/json_templates/' + sys.argv[1] + '.json', encoding='utf-8').read()
data = json.loads(json_data)

r = requests.post(webhookurl, json=data)
