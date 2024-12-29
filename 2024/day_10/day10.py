# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 22:47:33 2024

@author: Lim Jing
"""

input_map = {}
with open('input.txt') as f:
    for y, line in enumerate(f):
        for x, val in enumerate(line.strip()):
            input_map[(x,y)] = int(val)

map_shape = (x+1, y+1)
def get_neighbours(pos):
    x,y = pos
    outs = []
    if x > 0:
        outs.append((x-1, y))
    if x < map_shape[0]-1:
        outs.append((x+1, y))
    if y > 0:
        outs.append((x, y-1))
    if y < map_shape[1]-1:
        outs.append((x, y+1))
    return outs

reachable = {}  # memoized dict
def get_reachables(pos):
    if pos in reachable:
        return reachable[pos]

    val = input_map[pos]
    if val == 9:
        reachable[pos] = {(pos)}
    else:
        reach_set = set()
        neighbours = get_neighbours(pos)
        for neighbour in neighbours:
            if input_map[neighbour] == val+1:
                reach_set = reach_set.union(get_reachables(neighbour))
        reachable[pos] = reach_set

    return reachable[pos]


total = 0
for xi in range(map_shape[0]):
    for yi in range(map_shape[1]):
        if input_map[(xi,yi)] == 0:
            current = len(get_reachables((xi,yi)))
            # print(f'{(xi, yi)}: {current}')
            total += current

print(f'{total = }')


routes = {}  # memoized dict
def get_routes(pos):
    if pos in routes:
        return routes[pos]

    val = input_map[pos]
    if val == 9:
        routes[pos] = 1
    else:
        routes_from_here = 0
        neighbours = get_neighbours(pos)
        for neighbour in neighbours:
            if input_map[neighbour] == val+1:
                routes_from_here += get_routes(neighbour)
        routes[pos] = routes_from_here

    return routes[pos]

total_routes = 0
for xi in range(map_shape[0]):
    for yi in range(map_shape[1]):
        if input_map[(xi,yi)] == 0:
            current = get_routes((xi,yi))
            # print(f'{(xi, yi)}: {current}')
            total_routes += current

print(f'{total_routes = }')
