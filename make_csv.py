__author__ = 'andrew'

import codecs
import json
import numpy

raw_file = codecs.open('out_films.json', encoding='utf-8')
films = json.loads(raw_file.read())

fields_in_json = ['Actors', 'Director', 'Genre']
dims = {'Actors': {}, 'Director': {}, 'Genre': {}}
dims_num = {'Actors': 0, 'Director': 0, 'Genre': 0}

cur_dim = 0

for category in fields_in_json:
    for film in films:
        for elem in film[category]:
            if not elem in dims[category]:
                dims_num[category] += 1
                dims[category][elem] = 1
                cur_dim += 1
            else:
                dims[category][elem] += 1

directors = dims['Director']
top_directors_list = sorted([(k, v) for k, v in directors.items() if v > 2], key=lambda x: x[1], reverse=True)
top_d_map = {}
for k, v in top_directors_list:
    top_d_map[k] = v

actors = dims['Actors']
top_actors_list = sorted([(k, v) for k, v in actors.items() if v > 2], key=lambda x: x[1], reverse=True)
top_a_map = {}
for k, v in top_actors_list:
    top_a_map[k] = v


genres = dims['Genre']
top_genres_list = sorted([(k, v) for k, v in genres.items() if v > 3], key=lambda x: x[1], reverse=True)
top_g_map = {}
for k, v in top_genres_list:
    top_g_map[k] = v


films_to_choose = []
for f in films:
    o = 0
    for a in f['Actors']:
        if a in top_a_map:
            o += 1
    for d in f['Director']:
        if d in top_d_map:
            o += 1
    for g in f['Genre']:
        if g in top_g_map:
            o += 1
    if o > 4:
        films_to_choose.append(f)

print(len(films_to_choose))
dimensions = {}
tops = [i[0] for i in top_genres_list + top_actors_list + top_directors_list]
for i, val in enumerate(tops):
    dimensions[val] = i

coord_num = len(tops)

with codecs.open('films.csv', encoding='utf-8', mode='w') as csvfile:
    for f in films_to_choose:
        csvfile.write(f['Title'])
        csvfile.write(',')
        cur_vec = [0 for i in range(0, coord_num)]
        for c in fields_in_json:
            for elem in f[c]:
                if elem in dimensions:
                    cur_vec[dimensions[elem]] = 1
        csvfile.write(','.join([c for c in map(str, cur_vec)]))
        csvfile.write('\n')

with codecs.open('dimensions.csv', encoding='utf-8', mode='w') as csvfile:
    for i, val in enumerate(tops):
        csvfile.write('{},{}\n'.format(val, i + 1))




