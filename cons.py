# This is to save the data.json into a constant dictionary: DATA.

import json

DATA = json.load(open('data.json'))
DATA = dict((k, v) for k,v in DATA.items())