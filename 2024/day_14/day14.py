# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:53:57 2025

@author: Lim Jing
"""

from collections import defaultdict
import tqdm


width = 101
height = 103


robots = []
with open('input.txt') as f:
    for line in f.readlines():
        p, v = line.strip().split(' ')
        px, py = map(int, p.split('=')[1].split(','))
        vx, vy = map(int, v.split('=')[1].split(','))
        robots.append((px, py, vx, vy))


def get_quadrant(px, py):
    if py < (height-1)/2:
        if px < (width-1)/2:
            return 0
        if px > (width-1)/2:
            return 1
        else:
            return 4
    elif py > (height-1)/2:
        if px < (width-1)/2:
            return 2
        if px > (width-1)/2:
            return 3
        else:
            return 4
    else:
        return 4


quadrants = [0, 0, 0, 0, 0]
for robot in robots:
    px, py, vx, vy = robot
    npx = (px + 100*vx) % width
    npy = (py + 100*vy) % height
    quadrant = get_quadrant(npx, npy)
    quadrants[quadrant] += 1

prod = 1
for q in quadrants[:4]:
    prod *= q
print(f'{prod}')


# find longest vertical

longest = 0
idx = 0

def draw_picture(pos):
    for y in range(height):
        for x in range(width):
            if pos[(x,y)] > 0:
                print(pos[(x,y)], end='')
            else:
                print('.', end = '')
        print()

def get_positions(steps):
    positions = defaultdict(int)
    for robot in robots:
        px, py, vx, vy = robot
        npx = (px + i*vx) % width
        npy = (py + i*vy) % height
        positions[(npx, npy)] += 1
    return positions

for i in tqdm.trange(103*101):
    positions = get_positions(i)
    all_pos = set(positions.keys())
    c_longest = 0
    while len(all_pos) > 0:
        c_col = 1
        cx, cy = all_pos.pop()
        j = 1
        while positions[(cx, cy+j)] > 0:
            all_pos.remove((cx, cy+j))
            c_col += 1
            j += 1
        j = 1
        while positions[(cx, cy-j)] > 0:
            all_pos.remove((cx, cy-j))
            c_col += 1
            j += 1

        if c_col > c_longest:
            c_longest = c_col

    if c_longest > longest:
        longest = c_longest
        idx = i
        
        draw_picture(positions)
        print(longest)
        print(idx)
        input('next')
