#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# Our coordinate system for tiles puts the reference tile at (0, 0).
# The x-axis runs east-west, and the y-axis runs northwest-southeast:
#      nw    ne
# w    .     e
# sw   se
#
# Both locations (absolute) and directions (relative) are given as
# 2-tuples of int.


# str_dir: dict mapping strings to direction tuples.
str_dir = { "nw":( 0, 1),
            "ne":( 1, 1),
            "w" :(-1, 0),
            "e" :( 1, 0),
            "sw":(-1,-1),
            "se":( 0,-1) }


# add_tuples: given two 2-tuples of int, return their itemwise sum.
def add_tuples(tup1, tup2):
    assert isinstance(tup1, tuple)
    assert len(tup1) == 2
    assert isinstance(tup1[0], int)
    assert isinstance(tup1[1], int)
    assert isinstance(tup2, tuple)
    assert len(tup2) == 2
    assert isinstance(tup2[0], int)
    assert isinstance(tup2[1], int)
    return (tup1[0]+tup2[0], tup1[1]+tup2[1])


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = []
for line in sys.stdin:
    line = line.rstrip()
    dirs = []
    s = ""  # Direction string from input
    for c in line:
        s += c
        if c in { "e", "w" }:
            try:
                dirs.append(str_dir[s])
            except:
                assert False, f"Bad direction string: {s}"
            s = ""
    dataset.append(dirs)

# *** Do Computation ***

black_tiles = set()  # Set of locations of tiles with black side up
for dirs in dataset:
    loc = (0, 0)
    for d in dirs:
        loc = add_tuples(loc, d)
    black_tiles ^= {loc}  # Flip tile

# *** Print Answer ***

print(f"Answer: {len(black_tiles)}")

