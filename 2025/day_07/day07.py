# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 2025 12:01:33 AM

@author: Lim Jing
"""

import argparse
from collections import defaultdict

def main(args):
    board = {}
    with open(args.input_file) as f:
        row_id = -1
        for line in f:
            row_id += 1
            for col_id, char in enumerate(line.strip()):
                board[(row_id, col_id)] = char

    nrows = row_id + 1
    ncols = col_id + 1

    tachyon_cols = defaultdict(int)
    n_splits = 0

    #find start
    for col in range(ncols):
        if board[(0, col)] == 'S':
            tachyon_cols[col] = 1
            break

    for row in range(1, nrows):
        new_tachyon_cols = defaultdict(int)
        for col in tachyon_cols:
            if board[(row, col)] == '^':
                if col > 0:
                    new_tachyon_cols[col-1] += tachyon_cols[col]
                if col < ncols-1:
                    new_tachyon_cols[col+1] += tachyon_cols[col]
                n_splits += 1
            else:
                new_tachyon_cols[col] += tachyon_cols[col]
        tachyon_cols = new_tachyon_cols

    part_a = n_splits
    print(f'{part_a = }')

    part_b = sum(tachyon_cols.values())
    print(f'{part_b = }')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    args = parser.parse_args()

    main(args)
