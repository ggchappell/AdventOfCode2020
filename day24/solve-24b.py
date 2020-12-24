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


# dir_set: set of neighbor direction tuples.
dir_set = { ( 0, 1),
            ( 1, 1),
            (-1, 0),
            ( 1, 0),
            (-1,-1),
            ( 0,-1) }


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


# iterate: given set of locations of black-side-up tiles, do one daily
# iteration. New set of black-up tiles is returned; black_tiles is not
# modified.
def iterate(black_tiles):
    def count_black_nbrs(black_tiles, loc):
        count = 0
        for d in dir_set:
            if add_tuples(loc, d) in black_tiles:
                count += 1
        return count

    # Make list of white-up tiles that are adjacent to black-up tiles
    white_up_nbrs = set()
    for loc in black_tiles:
        for d in dir_set:
            nbr_loc = add_tuples(loc, d)
            if nbr_loc not in black_tiles:
                white_up_nbrs.add(nbr_loc)

    # Our revised black_tiles
    new_black_tiles = set()

    # Add black tiles that are not flipped to new set
    for loc in black_tiles:
        assert loc not in white_up_nbrs
        assert loc not in new_black_tiles
        c = count_black_nbrs(black_tiles, loc)
        if 1 <= c <= 2:
            new_black_tiles.add(loc)

    # Add white tiles that are flipped to new set
    for loc in white_up_nbrs:
        assert loc not in black_tiles
        assert loc not in new_black_tiles
        c = count_black_nbrs(black_tiles, loc)
        if c == 2:
            new_black_tiles.add(loc)

    # Return new set
    return new_black_tiles


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

num_iterations = 100
for _ in range(num_iterations):
    black_tiles = iterate(black_tiles)

# *** Print Answer ***

print(f"Answer: {len(black_tiles)}")

