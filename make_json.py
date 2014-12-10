__author__ = 'andrew'

import codecs
import json
import re

raw_file = codecs.open('films.json', encoding='utf-8')
out_file = codecs.open('out_films.json', encoding='utf-8', mode='w')

films = json.loads(raw_file.read())
raw_file.close()

fields = ['Actors', 'Director', 'Genre']

for f in films:
    for field in fields:
        f[field] = [a.strip() for a in f[field].split(',')]

out_file.write(json.dumps(films))
out_file.close()

