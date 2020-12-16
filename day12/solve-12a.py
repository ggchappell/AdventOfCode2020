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

commands = []
for line in sys.stdin:
    line = line.rstrip()
    assert len(line) > 0
    let = line[0]
    assert let in { "N", "S", "E", "W", "L", "R", "F" }
    num = int(line[1:])
    assert num > 0
    if let in { "L", "R" }:
        assert num in { 90, 180, 270 }
    commands.append((let, num))

# *** Do Computation ***

pos = [0, 0]
dir = [1, 0]
directions = { "N": [0, 1],
               "S": [0, -1],
               "E": [1, 0],
               "W": [-1, 0] }
for let, num in commands:
    if let in { "L", "R" }:
        num2 = num
        if let == "R":
            num2 = 360 - num
        if num2 == 90:
            dir = [-dir[1], dir[0]]
        elif num2 == 180:
            dir = [-dir[0], -dir[1]]
        elif num2 == 270:
            dir = [dir[1], -dir[0]]
        else:
            assert False
    else:
        directions["F"] = dir
        pos[0] += num * directions[let][0]
        pos[1] += num * directions[let][1]

# *** Print Answer ***

print(f"Answer: {abs(pos[0]) + abs(pos[1])}")

