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
way = [10, 1]
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
            way = [-way[1], way[0]]
        elif num2 == 180:
            way = [-way[0], -way[1]]
        elif num2 == 270:
            way = [way[1], -way[0]]
        else:
            assert False
    elif let == "F":
        pos[0] += num * way[0]
        pos[1] += num * way[1]
    elif let in { "N", "S", "E", "W" }:
        way[0] += num * directions[let][0]
        way[1] += num * directions[let][1]
    else:
        assert False

# *** Print Answer ***

print(f"Answer: {abs(pos[0]) + abs(pos[1])}")

