# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 09:09:53 2025

@author: Lim Jing
"""

from enum import Enum
import heapdict

board = {}

with open('input.txt') as f:
    row_id = -1
    for line in f:
        if line.startswith('#'):
            row_id += 1
            for col_id, char in enumerate(line.strip()):
                if char == '.':
                    board[(row_id, col_id)] = char
                if char == '#':
                    board[(row_id, col_id)] = char
                if char == 'S':
                    start_pos = (row_id, col_id)
                    board[(row_id, col_id)] = '.'
                if char == 'E':
                    end_pos = (row_id, col_id)
                    board[(row_id, col_id)] = '.'

board_size = (row_id+1, col_id+1)
maxsize = (board_size[0]*board_size[1]**2)*8

class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

    def clockwise(self):
        return Direction((self.value + 1)%len(Direction))

    def anticlockwise(self):
        return Direction((self.value - 1)%len(Direction))

    def flip(self):
        return Direction((self.value - 2)%len(Direction))


def print_board(board, board_size=board_size, indent=0):
    for row in range(board_size[0]):
        print('    '*indent, end='')
        for col in range(board_size[1]):
            print(board[(row, col)], end='')
        print()

def print_mult_board(final_dict, indent=0, pad=4):
    for row in range(board_size[0]):
        print('    '*indent, end='')
        for direction in Direction:
            for col in range(board_size[1]):
                try:

                    print(format(final_dict[((row, col), direction)], f'0{pad}'), end=' ')
                except KeyError:
                    print('-'*pad+' ', end='')
            print('')
        print()

def print_match_spots(match_spots, board, indent=0, line_num=False):
    for row in range(board_size[0]):
        if line_num:
            print(f'{row:03}:  ', end='')
        print('    '*indent, end='')
        for col in range(board_size[1]):
            if (row, col) in match_spots:
                print('O', end='')
            else:
                print(board[(row, col)], end='')
        print()


def forward(pos, direction):
    match direction:
        case Direction.LEFT:
            return (pos[0], pos[1]-1)
        case Direction.UP:
            return (pos[0]-1, pos[1])
        case Direction.RIGHT:
            return (pos[0], pos[1]+1)
        case Direction.DOWN:
            return (pos[0]+1, pos[1])

def backward(pos, direction):
    match direction:
        case Direction.LEFT:
            return (pos[0], pos[1]+1)
        case Direction.UP:
            return (pos[0]+1, pos[1])
        case Direction.RIGHT:
            return (pos[0], pos[1]-1)
        case Direction.DOWN:
            return (pos[0]-1, pos[1])

def dijkstra(start_pos, start_direction, end_pos, board, reverse=False):
    # init
    unvisited = heapdict.heapdict()
    for pos in board:
        for direction in Direction:
            if pos != start_pos or direction != start_direction:
                unvisited[(pos, direction)] = float('inf')
            else:
                unvisited[(pos, direction)] = 0

    final = {}

    while len(unvisited) > 0:
        curr = unvisited.popitem()
        # print(curr)
        (curr_pos, curr_dir), dist = curr

        if dist == float('inf'):
            final_val = min([final[(end_pos, direction)] for direction in Direction])
            return final_val, final

        final[(curr_pos, curr_dir)] = dist
        # if curr_pos == end_pos:
        #     return dist, final

        if not reverse:
            new_pos = forward(curr_pos, curr_dir)
        else:
            new_pos = backward(curr_pos, curr_dir)
        if board[new_pos] != '#' and (new_pos, curr_dir) in unvisited:
            prev = unvisited[(new_pos, curr_dir)]
            unvisited[(new_pos, curr_dir)] = min(prev, dist+1)
        if (curr_pos, curr_dir.clockwise()) in unvisited:
            prev = unvisited[(curr_pos, curr_dir.clockwise())]
            unvisited[(curr_pos, curr_dir.clockwise())] = min(prev, dist+1000)
        if (curr_pos, curr_dir.anticlockwise()) in unvisited:
            prev = unvisited[(curr_pos, curr_dir.anticlockwise())]
            unvisited[(curr_pos, curr_dir.anticlockwise())] = min(prev, dist+1000)

    raise ValueError('end pos is not reachable')


print_board(board)

# for i in range(board_size[0]-1, 0, -1):
#     for j in range(board_size[1]-1, 0, -1):
#         get_ans((i,j), end_pos, Direction(1))

best_dist, final_dict = dijkstra(start_pos, Direction.RIGHT, end_pos, board)
# print_mult_board(final_dict)
print(best_dist)


match_spots = set()
for direction in Direction:
    if final_dict[(end_pos, direction)] == best_dist:
        dist_rev, final_dict_rev = dijkstra(end_pos, direction, start_pos, board, reverse=True)

        for (pos, direc), curr_dist_rev in final_dict_rev.items():
            if final_dict[(pos, direc)] + curr_dist_rev == best_dist:
                match_spots.add(pos)

print_match_spots(match_spots, board)
print(len(match_spots))
