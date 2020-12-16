#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


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
    if line[0:4] == "mask":
        assert len(line) == 4 + 3 + 36
        mask_str = line[7:]
        assert len(mask_str) == 36
        mask_and = 0
        mask_or = 0
        power = 1
        for i in range(35, -1, -1):
            c = mask_str[i]
            if c != "0":
                mask_and = mask_and | power
            if c == "1":
                mask_or = mask_or | power
            power = power << 1
        commands.append((1, mask_and, mask_or))
    elif line[0:4] == "mem[":
        mo1 = re.search(r"^mem\[(\d+)\] = (\d+)$", line)
        assert mo1
        addr = int(mo1[1])
        value = int(mo1[2])
        commands.append((2, addr, value))
    else:
        assert False

# *** Do Computation ***

mem = {}
mask_and = 0
mask_or = 1
for cmd in commands:
    if cmd[0] == 1:
        mask_and = cmd[1]
        mask_or = cmd[2]
    elif cmd[0] == 2:
        addr = cmd[1]
        value = cmd[2]
        mem[addr] = (value & mask_and) | mask_or
    else:
        assert False

# *** Print Answer ***

total = 0
for addr in mem:
    total += mem[addr]
print(f"Answer: {total}")

