#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Argument must be JSON file to pretty print.")
    exit(-1)

import json
with open(sys.argv[1], 'r') as f:
    j = json.load(f)
    print(json.dumps(j, indent=2))
