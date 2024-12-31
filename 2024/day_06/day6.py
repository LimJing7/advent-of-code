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

def get_nxt_pos(pos, direction):
    i, j = pos
    direction = direction % 4

    if direction == Direction.UP:
        new_loc = (i-1, j)
    elif direction == Direction.RIGHT:
        new_loc = (i, j+1)
    elif direction == Direction.DOWN:
        new_loc = (i+1, j)
    elif direction == Direction.LEFT:
        new_loc = (i, j-1)

    return new_loc


input_map = {}
seen = defaultdict(set)
with open('input.txt') as f:
    for i, line in enumerate(f):
        for j, val in enumerate(line.strip()):
            input_map[(i,j)] = val
            if val == '^':
                input_map[(i,j)] = '.'
                start_loc = (i, j)
                ini_dir = Direction.UP


print(f'{len(input_map) = }')
sys.setrecursionlimit(len(input_map)*5)

def no_block_move(inp_map, position, direction: Direction, colored: int = 0, seen=None):
    if inp_map[position] == '.':
        inp_map[position] = 'X'
        colored += 1
    seen[position].add(direction % 4)

    new_loc = get_nxt_pos(position, direction)

    if new_loc not in inp_map:
        return colored, False
    elif direction in seen[new_loc]:
        return colored, True

    if inp_map[new_loc] == '#':
        return no_block_move(inp_map, position, (direction+1)%4, colored, seen)
    else:
        return no_block_move(inp_map, new_loc, direction, colored, seen)

part_a_map = copy.copy(input_map)
total_coloreds, looped = no_block_move(part_a_map, start_loc, Direction.UP, 0, seen)
print(f'{total_coloreds = }')

pos_loc = []
for k, v in part_a_map.items():
    if v == 'X' and k != start_loc:
        pos_loc.append(k)

n_looped = 0
for obs in pos_loc:
    new_map = copy.copy(input_map)
    new_map[obs] = '#'
    _, looped = no_block_move(new_map, start_loc, Direction.UP, 0, defaultdict(set))
    if looped:
        n_looped += 1

print(f'{n_looped = }')
