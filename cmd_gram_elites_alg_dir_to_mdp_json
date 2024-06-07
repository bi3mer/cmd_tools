#!/usr/bin/env python3

from os.path import join
from json import dump
import argparse

parser = argparse.ArgumentParser(description="Convert Gram-Elites output to a MDP graph")
parser.add_argument('--dir', type=str, default=".", help="Base directory for Gram-Elites algorithm type.")
parser.add_argument('--out', type=str, default="mdp", help="Name of the output json file. Do not include '.json'.")
args = parser.parse_args()

data = {}
with open(join(args.dir, "config_map_elites_generate_corpus_data.csv")) as f:
    f.readline() # skip first line

    for line in f.readlines():
        f_a, f_b, index, perf = line.strip().split(',')
        key = f'{f_b}_{f_a}_{index}'
        level_name = join(args.dir, 'levels', f'{key}.txt')

        with open(level_name) as f_level:
            data[int(f_a), int(f_b), int(index)] = {
                "R_d": int(perf),
                "lvl": [int(e) for e in f_level.readline().split(',')]
            }

def tuple_to_str(tup):
    return f'{tup[0]},{tup[1]},{tup[2]}'

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
                neighbors.append(tuple_to_str(new_key))
                index += 1
            else:
                break

    # update graph node
    if len(neighbors) > 0:
        nodes_with_neighbors += 1

        new_key = tuple_to_str(key)
        graph[new_key] = data[key]
        graph[new_key]['neighbors'] = neighbors

print(f'Nodes: {nodes_with_neighbors} / {len(data)}')

with open(f'{args.out}.json', 'w') as f:
    dump(graph, f)

print(f"Result file: ./{args.out}.json")
