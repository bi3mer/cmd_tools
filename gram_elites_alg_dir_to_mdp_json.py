#!/usr/bin/env python3

from os.path import join
from json import dump
import sys

if len(sys.argv) != 2:
    print("Include path to gram elites level directory in the command line argument")
    sys.exit(-1)

data = {}
with open(join(sys.argv[1], "config_map_elites_generate_corpus_data.csv")) as f:
    f.readline() # skip first line

    for line in f.readlines():
        f_a, f_b, index, perf = line.strip().split(',')
        key = f'{f_b}_{f_a}_{index}'
        level_name = join(sys.argv[1], 'levels', f'{key}.txt')

        with open(level_name) as f_level:
            data[int(f_a), int(f_b), int(index)] = {
                "R": perf,
                "lvl": f_level.readlines()
            }

nodes_with_neighbors = 0
DIR = [(-1,0), (1,0), (0,-1), (0,1)]
graph = {}
for key in data.keys():
    neighbors = []
    for (x,y) in DIR:
        new_x = key[0] + x
        new_y = key[1] + y

        index = 0
        while True:
            new_key = (new_x, new_y, index)

            if new_key in data:
                neighbors.append(str(new_key))
                index += 1
            else:
                break

    # update graph node
    if len(neighbors) > 0:
        nodes_with_neighbors += 1

        graph[str(key)] = data[key]
        graph[str(key)]['neighbors'] = neighbors

print(f'Nodes: {nodes_with_neighbors} / {len(data)}')

with open(join(sys.argv[1], 'mdp.json'), 'w') as f:
    dump(graph, f)

print("Result file: ./mdp.json")
