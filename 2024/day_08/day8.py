# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 16:54:10 2024

@author: Lim Jing
"""

from collections import defaultdict
import re

antenna_locs = defaultdict(list)
input_map = {}

max_x = 0
max_y = 0

with open('input.txt') as f:
    for y, line in enumerate(f):
        max_x = len(line.strip()) - 1
        for x, val in enumerate(line.strip()):
            if re.match(r'[a-zA-Z0-9]', val):
                input_map[(x,y)] = val
                antenna_locs[val].append((x,y))
    max_y = y

def check(x, y):
    if x < 0 or y < 0:
        return False
    if x > max_x or y > max_y:
        return False
    return True


def get_antinodes(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    ans = []

    if x1 < x2:
        if y1 < y2:
            mx1 = x1 - (x2-x1)
            my1 = y1 - (y2-y1)

            mx2 = x2 + (x2-x1)
            my2 = y2 + (y2-y1)

        elif y1 == y2:
            mx1 = x1 - (x2-x1)
            my1 = y1

            mx2 = x2 + (x2-x1)
            my2 = y1

        else:
            mx1 = x1 - (x2-x1)
            my1 = y1 + (y1-y2)

            mx2 = x2 + (x2-x1)
            my2 = y2 - (y1-y2)

    elif x1 == x2:
        if y1 < y2:
            mx1 = x1
            my1 = y1 - (y2-y1)

            mx2 = x1
            my2 = y2 + (y2-y1)

        elif y1 == y2:  # checking with itself produces nth
            return []

        else:
            mx1 = x1
            my1 = y2 - (y1-y2)

            mx2 = x1
            my2 = y1 + (y1-y2)

    else:
        if y1 < y2:
            mx1 = x2 - (x1-x2)
            my1 = y2 + (y2-y1)

            mx2 = x1 + (x1-x2)
            my2 = y1 - (y2-y1)

        elif y1 == y2:
            mx1 = x2 - (x1-x2)
            my1 = y1

            mx2 = x1 + (x1-x2)
            my2 = y1

        else:
            mx1 = x2 - (x1-x2)
            my1 = y2 - (y1-y2)

            mx2 = x1 + (x1-x2)
            my2 = y1 + (y1-y2)

    if check(mx1, my1):
        ans.append((mx1,my1))
    if check(mx2, my2):
        ans.append((mx2, my2))

    return ans


def get_all_integral(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    if x1 == x2 and y1 == y2:
        return []

    if x1 == x2:
        return [(x1, yi) for yi in range(max_y+1)]

    grad = (y2-y1)/(x2-x1)
    shift = y1 - grad * x1

    all_points = []
    for xi in range(max_x+1):
        yi = round(grad * xi + shift)
        if (y2-y1)*(xi-x1) == (yi-y1)*(x2-x1):
            all_points.append((xi,yi))

    return [(xi, yi) for (xi, yi) in all_points if check(xi, yi)]


def get_all_integral_v2(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    if x1 == x2 and y1 == y2:
        return []

    if x1 == x2:
        return [(x1, yi) for yi in range(max_y+1)]

    all_points = []

    delx = x1-x2
    dely = y1-y2

    xi = x1
    yi = y1

    while (xi >= 0 and xi <= max_x):
        all_points.append((xi, yi))
        xi = xi + delx
        yi = yi + dely
        
    while (xi >= 0 and xi <= max_x):
        all_points.append((xi, yi))
        xi = xi - delx
        yi = yi - dely

    return [(xi, yi) for (xi, yi) in all_points if check(xi, yi)]


antinodes = set()
for key, val in antenna_locs.items():
    let_ans = set()
    for pos1 in val:
        for pos2 in val:
            ans = get_antinodes(pos1, pos2)
            let_ans = let_ans.union(ans)
    # print(f'{key}: {let_ans}')
    antinodes = antinodes.union(let_ans)

print(f'{len(antinodes) = }')

v1 = {}
integral_antinodes = set()
for key, val in antenna_locs.items():
    let_ans = set()
    for pos1 in val:
        for pos2 in val:
            ans = get_all_integral(pos1, pos2)
            let_ans = let_ans.union(ans)
    v1[key] = let_ans
    # print(f'{key}: {let_ans}')
    integral_antinodes = integral_antinodes.union(let_ans)

print(f'{len(integral_antinodes) = }')

v2 = {}
integral_antinodes_v2 = set()
for key, val in antenna_locs.items():
    let_ans = set()
    for pos1 in val:
        for pos2 in val:
            ans = get_all_integral_v2(pos1, pos2)
            let_ans = let_ans.union(ans)
    v2[key] = let_ans
    # print(f'{key}: {let_ans}')
    integral_antinodes_v2 = integral_antinodes_v2.union(let_ans)

print(f'{len(integral_antinodes_v2) = }')
