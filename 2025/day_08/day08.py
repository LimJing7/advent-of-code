# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 2025 3:45:53 PM

@author: Lim Jing
"""

import argparse
import math

def main(args):
    positions = []
    with open(args.input_file) as f:
        for line in f:
            x, y, z = map(int, line.strip().split(','))
            positions.append((x, y, z))

    dist = {}
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            x1, y1, z1 = positions[i]
            x2, y2, z2 = positions[j]
            dist[(i, j)] = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

    groups = {i: {i} for i in range(len(positions))}

    counter = 0
    for (i, j), d in sorted(dist.items(), key=lambda x: x[1]):
        merged = groups[i] | groups[j]
        for k in merged:
            groups[k] = merged
        counter += 1
        if counter == 1000:
            unique_groups = set(map(frozenset, groups.values()))
            sizes = map(len, unique_groups)
            sizes = sorted(sizes, reverse=True)
            part_a = sizes[0] * sizes[1] * sizes[2]
            print(f'{part_a = }')

        if len(merged) == len(positions):
            part_b = positions[i][0] * positions[j][0]
            print(f'{part_b = }')
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    args = parser.parse_args()

    main(args)
