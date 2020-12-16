#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import copy         # .deepcopy


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def iterate(grid):
    def sees_occupied01(r, c, dr, dc):
        nr = r
        nc = c
        while True:
            nr += dr
            nc += dc
            if nr < 0 or nr >= len(grid):
                return 0
            if nc < 0 or nc >= len(grid[0]):
                return 0
            ch = grid[nr][nc]
            if ch == ".":
                continue
            elif ch == "L":
                return 0
            else:
                assert ch == "#"
                return 1

    def count_occupied_nbrs(r, c):
        return (sees_occupied01(r, c, -1, -1) +
                sees_occupied01(r, c, -1,  0) +
                sees_occupied01(r, c, -1,  1) +
                sees_occupied01(r, c,  0, -1) +
                sees_occupied01(r, c,  0,  1) +
                sees_occupied01(r, c,  1, -1) +
                sees_occupied01(r, c,  1,  0) +
                sees_occupied01(r, c,  1,  1))

    new_grid = copy.deepcopy(grid)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            ch = grid[r][c]
            if ch == ".":
                continue
            occupied_count = count_occupied_nbrs(r, c)
            if ch == "L" and occupied_count == 0:
                new_grid[r][c] = "#"
            if ch == "#" and occupied_count >= 5:
                new_grid[r][c] = "L"
    return new_grid


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

seat_grid = []
first_row = True
for line in sys.stdin:
    line = line.rstrip()
    if first_row:
        width = len(line)
        first_row = False
    assert len(line) == width
    seat_row = []
    for c in line:
        assert c == "." or c == "L"
        seat_row.append(c)
    seat_grid.append(seat_row)
assert len(seat_grid) > 0
assert len(seat_grid[0]) > 0

# *** Do Computation ***

while True:
    new_grid = iterate(seat_grid)
    if new_grid == seat_grid:
        break
    seat_grid = new_grid

total = 0
for row in seat_grid:
    for c in row:
        if c == "#":
            total += 1

# *** Print Answer ***

print(f"Answer: {total}")

