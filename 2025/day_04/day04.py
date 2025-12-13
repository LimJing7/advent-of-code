# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 2025 9:19:18 PM

@author: Lim Jing
"""

import argparse
import copy

def get_and_rmv_accessible(board, nrows, ncols):

    new_board = copy.copy(board)

    n_accessible = 0
    for row_id in range(nrows):
        for col_id in range(ncols):
            if board[(row_id, col_id)] == '@':
                n_rolls = 0
                for dy in range(-1,2):
                    for dx in range(-1,2):
                        if board.get((row_id+dy, col_id+dx), '.') == '@':
                            n_rolls += 1
                if n_rolls < 5:
                    n_accessible += 1
                    new_board[(row_id, col_id)] = '.'

    return n_accessible, new_board



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

    part_a, _ = get_and_rmv_accessible(board, nrows, ncols)

    print(f'{part_a = }')

    n_rmved = 0
    curr_board = board
    while True:
        new_rmv, new_board = get_and_rmv_accessible(curr_board, nrows, ncols)
        if new_rmv == 0:
            break
        else:
            n_rmved += new_rmv
            curr_board = new_board

    print(f'part_b = {n_rmved}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    args = parser.parse_args()

    main(args)
