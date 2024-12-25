# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:48:23 2024

@author: Lim Jing
"""

input_list = []


part_a_kept_sum = 0
part_b_kept_sum = 0

with open('input.txt') as f:
    for i, line in enumerate(f):
        vals = line.strip().split()
        tot = int(vals[0][:-1])
        rest = [int(i) for i in vals[1:]]

        working_a = [rest[0]]
        working_b = [rest[0]]
        for v in rest[1:]:
            new_a = []
            for t in working_a:
                s = t+v
                p = t*v
                if s<= tot:
                    new_a.append(s)
                if p <= tot:
                    new_a.append(p)
            new_b = []
            for t in working_b:
                s = t+v
                p = t*v
                c = int(str(t)+str(v))
                if s<= tot:
                    new_b.append(s)
                if p <= tot:
                    new_b.append(p)
                if c <= tot:
                    new_b.append(c)
            working_a = new_a
            working_b = new_b

        if tot in working_a:
            part_a_kept_sum += tot

        if tot in working_b:
            part_b_kept_sum += tot

print(f'{part_a_kept_sum = }')
print(f'{part_b_kept_sum = }')
