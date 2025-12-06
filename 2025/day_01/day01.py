# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 15:58:48 2025

@author: Lim Jing
"""

current = 50
part_a = 0
part_b = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        # mult = -1 if line[0] == 'L' else 1
        if line[0] == 'L':
            mult = -1
            if current == 0:
                current = 100
        else:
            mult = 1
        dist = int(line[1:])
        current += mult*dist
        reps = current // 100
        part_b += abs(reps)
        current = current % 100
        if current == 0:
            part_a += 1
            if mult == -1:
                part_b += 1

        # print(line, current, part_b)

print(f'{part_a = }')
print(f'{part_b = }')
