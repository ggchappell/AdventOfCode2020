#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import copy         # .deepcopy


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def iterate(grid):
    def is_occupied01(r, c):
        if r < 0 or r >= len(grid):
            return 0
        if c < 0 or c >= len(grid[0]):
            return 0
        if grid[r][c] == "." or grid[r][c] == "L":
            return 0
        return 1

    def count_occupied_nbrs(r, c):
        return (is_occupied01(r-1, c-1)
                + is_occupied01(r-1, c)
                + is_occupied01(r-1, c+1)
                + is_occupied01(r,   c-1)
                + is_occupied01(r,   c+1)
                + is_occupied01(r+1, c-1)
                + is_occupied01(r+1, c)
                + is_occupied01(r+1, c+1) )

    new_grid = copy.deepcopy(grid)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            ch = grid[r][c]
            if ch == ".":
                continue
            occupied_count = count_occupied_nbrs(r, c)
            if ch == "L" and occupied_count == 0:
                new_grid[r][c] = "#"
            if ch == "#" and occupied_count >= 4:
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

