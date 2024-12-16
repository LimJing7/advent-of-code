# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:28:03 2024

@author: Lim Jing
"""
from collections import defaultdict
import copy
from enum import IntEnum
import sys

class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

input_map = {}
seen = defaultdict(set)
with open('test_inp.txt') as f:
    for i, line in enumerate(f):
        for j, val in enumerate(line.strip()):
            input_map[(i,j)] = val
            if val == '^':
                input_map[(i,j)] = 'X'
                start_loc = (i, j)
                ini_dir = Direction.UP
                seen[(i,j)].add(Direction.UP)


print(f'{len(input_map) = }')
sys.setrecursionlimit(len(input_map)*5)

def no_block_move(inp_map, position, direction: Direction, colored: int = 1, seen=None):
    i, j = position
    direction = direction % 4

    if direction == Direction.UP:
        new_loc = (i-1, j)
    elif direction == Direction.RIGHT:
        new_loc = (i, j+1)
    elif direction == Direction.DOWN:
        new_loc = (i+1, j)
    elif direction == Direction.LEFT:
        new_loc = (i, j-1)

    if new_loc not in inp_map:
        return colored, False
    elif direction in seen[new_loc]:
        return colored, True
    else:
        seen[new_loc].add(direction)

    if inp_map[new_loc] == '#':
        return no_block_move(inp_map, position, direction+1, colored, seen)
    elif inp_map[new_loc] == '.':
        inp_map[new_loc] = 'X'
        return no_block_move(inp_map, new_loc, direction, colored+1, seen)
    elif inp_map[new_loc] == 'X':
        return no_block_move(inp_map, new_loc, direction, colored, seen)

def block_move(inp_map, position, direction: Direction, colored: int = 1, seen=None):
    i, j = position
    direction = direction % 4

    if direction == Direction.UP:
        new_loc = (i-1, j)
    elif direction == Direction.RIGHT:
        new_loc = (i, j+1)
    elif direction == Direction.DOWN:
        new_loc = (i+1, j)
    elif direction == Direction.LEFT:
        new_loc = (i, j-1)

    seen[new_loc].add(direction)

    if new_loc not in inp_map:
        return set()
    elif inp_map[new_loc] == '#':
        return block_move(inp_map, position, direction+1, colored, seen)
    else:
        new_map = copy.copy(inp_map)
        new_map[new_loc] = '#'
        new_seen = copy.copy(seen)
        _, looped = no_block_move(new_map, position, direction+1, colored, new_seen)
        nobs = block_move(inp_map, new_loc, direction, colored, seen)

        if looped:
            return nobs.union({new_loc})
        else:
            return nobs

total_coloreds, looped = no_block_move(input_map, start_loc, Direction.UP, 1, seen)
print(f'{total_coloreds = }')

n_obs = block_move(input_map, start_loc, Direction.UP, 1, seen)
print(f'{n_obs = }')
print(f'{len(n_obs) = }')
