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

group_lines = []
record_str = ""
for line in sys.stdin:
    line = line.rstrip()
    if line:
        record_str += line
        continue
    group_lines.append(record_str)
    record_str = ""  # Prep for next
if record_str:
    group_lines.append(record_str)

# *** Do Computation ***

total = 0
for g in group_lines:
    total += len(set(g))  # Add no. of distinct chars in g

# *** Print Answer ***

print(f"Answer: {total}")

