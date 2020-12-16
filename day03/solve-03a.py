#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# (NONE)


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

tree_count = 0
col = 0
for row in range(1, len(tmap)):
    col += 3
    if tmap[row][col % row_len] == "#":
        tree_count += 1

# *** Print Answer ***

print(f"Answer: {tree_count}")


