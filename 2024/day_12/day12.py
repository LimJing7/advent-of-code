# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:35:10 2024

@author: Lim Jing
"""

from collections import defaultdict

input_map = {}
with open('input.txt') as f:
    for y, line in enumerate(f):
        for x, val in enumerate(line.strip()):
            input_map[(x,y)] = val
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

def get_fence(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    hf=-1
    vf=-1

    if x1 == x2:
        if y1 == y2-1:
            hf = (x1, y1+0.5)
        else:
            hf = (x1, y1-0.5)
    else:
        if x1 == x2-1:
            vf = (x1+0.5, y1)
        else:
            vf = (x1-0.5, y1)

    return hf, vf

plot_ids = {}
unions = {}
areas = defaultdict(int)
perimeters = defaultdict(int)
h_fences = defaultdict(list)
v_fences = defaultdict(list)

next_plot_id = 0
for xi in range(map_shape[0]):
    for yi in range(map_shape[1]):
        plant_type = input_map[(xi, yi)]
        neighbours = get_neighbours((xi, yi))
        c_union = set()
        plot_id = -1
        peri = 4
        h_f = [(xi,yi-0.5), (xi,yi+0.5)]
        v_f = [(xi-0.5,yi), (xi+0.5,yi)]
        for neighbour in neighbours:
            if plant_type == input_map[neighbour]:
                peri -= 1
                hf, vf = get_fence((xi, yi), neighbour)
                if hf == -1:
                    v_f.remove(vf)
                else:
                    h_f.remove(hf)
                try:
                    n_id = plot_ids[neighbour]
                    if plot_id == -1:
                        plot_id = n_id
                    elif plot_id != n_id:
                        c_union.add(n_id)
                        try:
                            c_union.update(unions[n_id])
                        except KeyError:
                            pass
                except KeyError:
                    pass
        if plot_id == -1:
            plot_id = next_plot_id
            next_plot_id += 1
        plot_ids[(xi, yi)] = plot_id
        c_union.add(plot_id)
        try:
            c_union.update(unions[plot_id])
        except KeyError:
            pass

        if len(c_union) > 1:
            for pid in c_union:
                try:
                    unions[pid] = c_union - {pid}
                except KeyError:
                    pass

        areas[plot_id] += 1
        perimeters[plot_id] += peri
        if len(h_f) > 0:
            h_fences[plot_id].extend(h_f)
        if len(v_f) > 0:
            v_fences[plot_id].extend(v_f)

for plot_id, union in unions.items():
    for c_id in union:
        areas[plot_id] += areas[c_id]
        areas[c_id] = 0
        perimeters[plot_id] += perimeters[c_id]
        perimeters[c_id] = 0
        h_fences[plot_id].extend(h_fences[c_id])
        h_fences[c_id] = []
        v_fences[plot_id].extend(v_fences[c_id])
        v_fences[c_id] = []

total_price = 0
for k in areas:
    total_price += areas[k] * perimeters[k]

print(f'{total_price = }')

total_price_p2 = 0
for k, area in areas.items():
    if area == 0:
        continue

    n_sides = 0

    hf = sorted(h_fences[k])
    vf = sorted(v_fences[k])
    for c_hf in hf:
        af = (c_hf[0]+0.5, c_hf[1]-0.5)
        bf = (c_hf[0]+0.5, c_hf[1]+0.5)
        if af in vf or bf in vf:
            n_sides += 1
    for c_vf in vf:
        lf = (c_vf[0]-0.5, c_vf[1]+0.5)
        rf = (c_vf[0]+0.5, c_vf[1]+0.5)
        if lf in hf or rf in hf:
            n_sides += 1

    total_price_p2 += area * n_sides

print(f'{total_price_p2 = }')
