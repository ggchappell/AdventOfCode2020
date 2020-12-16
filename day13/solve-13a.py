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

busses = []
line = sys.stdin.readline()
line = line.rstrip()
earliest = int(line)
assert(earliest >= 0)
line = sys.stdin.readline()
line = line.rstrip()
bs = line.split(",")
for b in bs:
    if b == "x":
        continue
    bnum = int(b)
    assert bnum > 0
    busses.append(bnum)

# *** Do Computation ***

best_times = []
for bnum in busses:
    q = earliest // bnum
    r = earliest % bnum
    best = q * bnum
    if r > 0:
        best += bnum
    best_times.append(best)
assert len(busses) == len(best_times)
assert len(busses) > 0
overall_best_time = 0
result = 0
for i in range(len(busses)):
    if i == 0 or best_times[i] < overall_best_time:
        overall_best_time = best_times[i]
        result = busses[i] * (best_times[i] - earliest)

# *** Print Answer ***

print(f"Answer: {result}")

