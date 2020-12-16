#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import itertools    # .combinations


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================

def gcd(a, b):
    assert a >= 0 and b >= 0 and not (a == 0 and b == 0)
    if a == 0:
        return b
    return gcd(b % a, a)


# solve_two
# We wish to solve this system:
#   x % d1 == r1
#   x % d2 == r2
# for d1, d2 relatively prime positive integers, r1, r2, nonnegative
# integers with 0 <= r1 < d1 and 0 <= r2 < d2, and x an unknown
# nonnegative integer.
# Solution: x % (d1*d2) == r3 with 0 <= r3 < d1*d2.
# Return value is r3.
def solve_two(d1, r1, d2, r2):
    assert isinstance(d1, int)
    assert isinstance(r1, int)
    assert isinstance(d2, int)
    assert isinstance(r2, int)
    assert d1 > 0
    assert d2 > 0
    assert gcd(d1, d2) == 1
    assert 0 <= r1 < d1
    assert 0 <= r2 < d2

    r3 = r1
    prod = d1*d2
    while True:
        assert r3 < prod
        if r3 % d2 == r2:
            return r3
        r3 += d1

def bnum_remainder(bnum_offset):
    bnum, offset = bnum_offset
    assert 0 <= offset
    offset = offset % bnum
    if offset == 0:
        return (bnum, 0)
    return (bnum, bnum-offset)


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
for i, b in enumerate(bs):
    if b == "x":
        continue
    bnum = int(b)
    assert bnum > 0
    busses.append((bnum, i))

assert len(busses) > 0
for a, b in itertools.combinations([ a for a,_ in busses ], 2):
    assert gcd(a, b) == 1  # False? Solve the problem differently

# *** Do Computation ***

#print(busses)
busses_with_remainder = [ bnum_remainder(bo) for bo in busses ]
d, r = busses_with_remainder[0]
for dd, rr in busses_with_remainder[1:]:
    d, r = d*dd, solve_two(d, r, dd, rr)

# *** Print Answer ***

print(f"Answer: {r}")

