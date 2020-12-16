#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def count_trees(tmap, skip):
    assert len(tmap) > 0
    row_len = len(tmap[0])
    assert len(skip) == 2
    rt = skip[0]
    assert 1 <= rt
    dn = skip[1]
    assert 1 <= dn

    tree_count = 0
    row = 0
    col = 0
    while True:
        row += dn
        if row >= len(tmap):
            break
        col += rt
        if tmap[row][col % row_len] == "#":
            tree_count += 1
    return tree_count


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

tmap = []
row_len = None
for line in sys.stdin:
    line = line.rstrip()
    if row_len is None:
        row_len = len(line)
    else:
        assert len(line) == row_len

    tmap_line = []
    for c in line:
        assert c == "." or c == "#"
        tmap_line.append(c)
    tmap.append(tmap_line)
assert row_len is not None

# *** Do Computation ***

skips = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

prod = 1
for skip in skips:
    prod *= count_trees(tmap, skip)

# *** Print Answer ***

print(f"Answer: {prod}")

