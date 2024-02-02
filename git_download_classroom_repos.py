#!/usr/bin/env python3

import sys
import csv
import subprocess

if len(sys.argv) != 2:
    print('Command line argument required: grade csv file from github classroom.')
    sys.exit(-1)

filename = sys.argv[1]
processes = []
with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['student_repository_url'])
        student_repo = row['student_repository_url']
        processes.append(subprocess.Popen(['git', 'clone', student_repo]))

for p in processes:
    p.wait() # wait till done

print("DONE")
