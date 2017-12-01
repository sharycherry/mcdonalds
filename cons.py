import json

DATA = json.load(open('data.json'))
DATA = dict((k, v) for k,v in DATA.items())