#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import itertools    # .product


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def count_active_nbrs(active_set, k):
    count = 0
    for offset in itertools.product((-1,0,1), repeat=4):
        if offset == (0,0,0,0):
            continue
        nbr = (k[0]+offset[0],k[1]+offset[1],k[2]+offset[2],k[3]+offset[3])
        if nbr in active_set:
            count += 1
    return count


def iterate(active_set):
    # Make set of inactive neighbors of active cubes
    inactive_to_check = set()
    for k in active_set:
        for offset in itertools.product((-1,0,1), repeat=4):
            if offset == (0,0,0,0):
                continue
            nbr = (k[0]+offset[0],k[1]+offset[1],k[2]+offset[2],k[3]+offset[3])
            if nbr in active_set:
                continue
            inactive_to_check.add(nbr)
    # Make new active set
    # (1) Check currently inactive cubes
    new_active_set = set()
    for key in active_set:
        if 2 <= count_active_nbrs(active_set, key) <= 3:
            new_active_set.add(key)
    # (2) Check currently inactive cubes next to active cubes
    for key in inactive_to_check:
        if count_active_nbrs(active_set, key) == 3:
            new_active_set.add(key)
    # DONE
    return new_active_set


def count_active_cubes(active_set):
    return len(active_set)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

active_set = set()
z = 0
w = 0
y = 0
for line in sys.stdin:
    line = line.rstrip()
    for x, c in enumerate(line):
        if c == "#":
            key = (x, y, z, w)
            assert key not in active_set
            active_set.add(key)
    y += 1

# *** Do Computation ***

num_iterations = 6
for i in range(num_iterations):
    active_set = iterate(active_set)
result = count_active_cubes(active_set)

# *** Print Answer ***

print(f"Answer: {result}")

