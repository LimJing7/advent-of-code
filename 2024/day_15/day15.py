# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 09:09:53 2025

@author: Lim Jing
"""
from collections import defaultdict
import copy

board = defaultdict((lambda: '.'))
big_board = defaultdict((lambda: '.'))
moves = []

with open('input.txt') as f:
    row_id = -1
    for line in f:
        if line.startswith('#'):
            row_id += 1
            for col_id, char in enumerate(line.strip()):
                if char == 'O':
                    board[(row_id, col_id)] = char
                    big_board[(row_id, col_id*2)] = '['
                    big_board[(row_id, col_id*2+1)] = ']'
                if char == '#':
                    board[(row_id, col_id)] = char
                    big_board[(row_id, col_id*2)] = char
                    big_board[(row_id, col_id*2+1)] = char
                if char == '@':
                    start_pos = (row_id, col_id)
                    big_start_pos = (row_id, col_id*2)

        else:
            moves.extend(list(line.strip()))

board_size = (row_id+1, col_id+1)
big_board_size = (row_id+1, col_id*2+2)


def print_board(board, curr, board_size=board_size, indent=0):
    for row in range(board_size[0]):
        print('    '*indent, end='')
        for col in range(board_size[1]):
            if (row, col) == curr:
                print('@', end='')
            else:
                print(board[(row, col)], end='')
        print()

def check_board(board):
    for key in board:
        if board[key] == '[':
            if not board[(key[0], key[1]+1)] == ']':
                return False
        elif board[key] == ']':
            if not board[(key[0], key[1]-1)] == '[':
                return False
    return True

def oob(pos, board_size=board_size):
    if pos[0] <= 0 or pos[1] <= 0:
        return True
    if pos[0] >= board_size[0]-1 or pos[1] >= board_size[1]-1:
        return True
    return False

def compute_gps(board):
    total = 0
    for (row, col), item in board.items():
        if item == 'O' or item=='[':
            total += 100*row + col
    return total

def make_move(board, pos, direction, board_size=board_size):
    (row_pos, col_pos) =  pos

    if direction == '<':
        new_pos = (row_pos, col_pos-1)
    elif direction == '^':
        new_pos = (row_pos-1, col_pos)
    elif direction == '>':
        new_pos = (row_pos, col_pos+1)
    elif direction == 'v':
        new_pos = (row_pos+1, col_pos)

    if oob(new_pos, board_size):
        return board, pos


    if board[new_pos] == '#':
        return board, pos
    elif board[new_pos] == '.':
        new_board = copy.copy(board)
        new_board[new_pos] = board[pos]
        new_board[pos] = '.'
        return new_board, new_pos
    elif board[new_pos] == 'O' or board[new_pos] == '[' or board[new_pos] == ']':
        n_board, n_pos = make_move(board, new_pos, direction, board_size)
        if n_pos == new_pos:
            return board, pos
        new_board = copy.copy(n_board)
        new_board[new_pos] = board[pos]
        new_board[pos] = '.'
        return new_board, new_pos


def merge(board_1, board_2, orig_board):
    new_board = defaultdict((lambda: '.'))
    for key in set(board_1.keys()).union(set(board_2.keys())):
        if board_1[key] == board_2[key]:
            new_board[key] = board_1[key]
        elif board_1[key] == orig_board[key]:
            new_board[key] = board_2[key]
        elif board_2[key] == orig_board[key]:
            new_board[key] = board_1[key]
        elif board_1[key] == '.':  ## handle cases where all 3 dont match
            new_board[key] = board_2[key]
        elif board_2[key] == '.':
            new_board[key] = board_1[key]

    return new_board


def make_move_big(board, pos, direction, indent=0):
    (row_pos, col_pos) =  pos

    if direction == '<':
        new_pos = (row_pos, col_pos-1)
    elif direction == '^':
        new_pos = (row_pos-1, col_pos)
    elif direction == '>':
        new_pos = (row_pos, col_pos+1)
    elif direction == 'v':
        new_pos = (row_pos+1, col_pos)

    if oob(new_pos, big_board_size):
        return board, pos


    if board[new_pos] == '#':
        return board, pos
    elif board[new_pos] == '.':
        new_board = copy.copy(board)
        new_board[new_pos] = board[pos]
        new_board[pos] = '.'
        return new_board, new_pos
    elif (board[new_pos] == '[' or board[new_pos] == ']') and (direction == '<' or direction == '>'):
        n_board, n_pos = make_move(board, new_pos, direction, big_board_size)
        if n_pos == new_pos:
            return board, pos
        new_board = copy.copy(n_board)
        new_board[new_pos] = board[pos]
        new_board[pos] = '.'
        return new_board, new_pos

    elif board[new_pos] == '[':
        # print('*'*120)
        # print('orig')
        # print_board(board, (0,0), big_board_size, indent=indent)
        new_adj_pos = (new_pos[0], new_pos[1]+1)
        n_board_0, n_pos_0 = make_move_big(board, new_pos, direction, indent+1)
        # print('board_0')
        # print_board(n_board_0, (0,0), big_board_size, indent=indent)
        n_board_1, n_pos_1 = make_move_big(board, new_adj_pos, direction, indent+1)
        # print('board_1')
        # print_board(n_board_1, (0,0), big_board_size, indent=indent)
        if n_pos_0 == new_pos or n_pos_1 == new_adj_pos:
            return board, pos
        else:
            new_board = merge(n_board_0, n_board_1, board)
            # print('merged')
            # print_board(new_board, (0,0), big_board_size, indent=indent)
            new_board[new_pos] = board[pos]
            new_board[pos] = '.'
            # print('shifted')
            # print_board(new_board, (0,0), big_board_size, indent=indent)
            if board[pos] == '[':
                my_adj_pos = (pos[0], pos[1]+1)
                new_my_adj_pos = (new_pos[0], new_pos[1]+1)
                new_board[new_my_adj_pos] = board[my_adj_pos]
                new_board[my_adj_pos] = '.'
            elif board[pos] == ']':
                my_adj_pos = (pos[0], pos[1]-1)
                new_my_adj_pos = (new_pos[0], new_pos[1]-1)
                new_board[new_my_adj_pos] = board[my_adj_pos]
                new_board[my_adj_pos] = '.'
            # print('adj shifted')
            # print_board(new_board, (0,0), big_board_size, indent=indent)
            return new_board, new_pos
    elif board[new_pos] == ']':
        # print('*'*120)
        # print('orig')
        # print_board(board, (0,0), big_board_size, indent=indent)
        new_adj_pos = (new_pos[0], new_pos[1]-1)
        n_board_0, n_pos_0 = make_move_big(board, new_pos, direction, indent+1)
        # print('board_0')
        # print_board(n_board_0, (0,0), big_board_size, indent=indent)
        n_board_1, n_pos_1 = make_move_big(board, new_adj_pos, direction, indent+1)
        # print('board_1')
        # print_board(n_board_1, (0,0), big_board_size, indent=indent)
        if n_pos_0 == new_pos or n_pos_1 == new_adj_pos:
            return board, pos
        else:
            new_board = merge(n_board_0, n_board_1, board)
            # print('merged')
            # print_board(new_board, (0,0), big_board_size, indent=indent)
            new_board[new_pos] = board[pos]
            new_board[pos] = '.'
            # print('shifted')
            # print_board(new_board, (0,0), big_board_size, indent=indent)
            if board[pos] == '[':
                my_adj_pos = (pos[0], pos[1]+1)
                new_my_adj_pos = (new_pos[0], new_pos[1]+1)
                new_board[new_my_adj_pos] = board[my_adj_pos]
                new_board[my_adj_pos] = '.'
            elif board[pos] == ']':
                my_adj_pos = (pos[0], pos[1]-1)
                new_my_adj_pos = (new_pos[0], new_pos[1]-1)
                new_board[new_my_adj_pos] = board[my_adj_pos]
                new_board[my_adj_pos] = '.'
            # print('adj shifted')
            # print_board(new_board, (0,0), big_board_size, indent=indent)
            return new_board, new_pos

nb = board
np = start_pos
for move_i in moves:
    nb, np = make_move(nb, np, move_i)

print_board(board, start_pos)
print_board(nb, np)
print(compute_gps(nb))

print('\n')

nb = big_board
np = big_start_pos
for move_i, movement in enumerate(moves):
    nb, np = make_move_big(nb, np, movement)
print_board(big_board, big_start_pos, big_board_size)
print_board(nb, np, big_board_size)
print(compute_gps(nb))
