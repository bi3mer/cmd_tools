#!/usr/bin/env python3

import os

COMPILER="g++"

SOURCE="./src/*.cpp"

# You can can add other arguments as you see fit.
# What does the "-D MAC" command do? 
ARGUMENTS="-D MAC -std=c++20 -shared -undefined dynamic_lookup `pkg-config --libs sdl2`" 

# Which directories do we want to include.
INCLUDE_DIR="-I ./include/ -I./pybind11/include/ -I/Library/Frameworks/SDL2.framework/Headers `python3.9 -m pybind11 --includes`"

# What libraries do we want to include
LIBRARIES="-F/Library/Frameworks `python3.9-config --ldflags`"

# The name of our executable
EXECUTABLE="mygameengine.so"

# Build a string of our compile commands that we run in the terminal
compileString=COMPILER+" "+ARGUMENTS+" -o "+EXECUTABLE+" "+" "+INCLUDE_DIR+" "+SOURCE+" "+LIBRARIES

# Print out the compile string
print(compileString)

# Run our command
os.system(compileString)
