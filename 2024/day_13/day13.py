# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 10:49:36 2025

@author: Lim Jing
"""

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


questions = []
with open('input.txt') as f:
    while True:
        try:
            a = list(map(lambda x: int(x.split('+')[1]), f.readline().split(': ')[1].split(', ')))
            b = list(map(lambda x: int(x.split('+')[1]), f.readline().split(': ')[1].split(', ')))
            A = np.array([a,b], dtype='int64').T
            p = np.array(list(map(lambda x: int(x.split('=')[1]), f.readline().split(': ')[1].split(', '))), dtype='int64')
            f.readline()
            questions.append((A, p))
        except IndexError:
            break

c = np.array([3, 1], dtype='int64')
cost = 0
for question in questions:
    A, p = question
    lc = LinearConstraint(A, p, p)
    res = milp(c=c, constraints=lc, integrality=np.ones_like(c), bounds=Bounds(0, 120))
    if res.success:
        cost += int(res.fun)

print(f'{cost = }')


cost = 0
for question in questions:
    A, p = question
    p += 10000000000000

    AB_mat = np.linalg.inv(A)
    new_p = AB_mat @ p
    if np.allclose(np.round(new_p) @ A.T-p, 0):
        cost += round(new_p @ c)

print(f'{cost = }')
