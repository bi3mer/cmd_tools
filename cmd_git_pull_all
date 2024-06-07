#!/usr/bin/env python3

import subprocess
import os

processes = []
for d in os.listdir():
    if os.path.isdir(d):
        print(d)
        processes.append(subprocess.Popen(['git', 'pull'], cwd=os.path.join('.', d)))

for p in processes:
    p.wait()

print('\n\nDONE')
