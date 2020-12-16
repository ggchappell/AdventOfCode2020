#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def is_valid_bps(bps):
    if not isinstance(bps, str):
        return False
    if len(bps) != 10:
        return False
    for c in bps[0:7]:
        if c != "F" and c != "B":
            return False
    for c in bps[7:]:
        if c != "R" and  c != "L":
            return False
    return True


def bps_to_info(bps):
    assert is_valid_bps(bps)

    # Find row
    r1 = 0
    r2 = 128
    for c in bps[0:7]:
        d = r2 - r1
        assert d % 2 == 0
        if c == "F":
            r2 -= d//2
        elif c == "B":
            r1 += d//2
        else:
            assert False
    assert r2 == r1+1

    # Find column
    c1 = 0
    c2 = 8
    for c in bps[7:]:
        d = c2 - c1
        assert d % 2 == 0
        if c == "L":
            c2 -= d//2
        elif c == "R":
            c1 += d//2
        else:
            assert False
    assert c2 == c1+1

    return r1, c1, r1*8 + c1


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

bpss = []
for line in sys.stdin:
    line = line.rstrip()
    assert(is_valid_bps(line))
    bpss.append(line)

# *** Do Computation ***

max_id = None
for bps in bpss:
    info = bps_to_info(bps)
    seat_id = info[2]
    if max_id is None or seat_id > max_id:
        max_id = seat_id

# *** Print Answer ***

print(f"Answer: {max_id}")

