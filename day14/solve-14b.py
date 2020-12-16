#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search
import itertools    # .combinations, .chain


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# From itertools docs
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r)
                                         for r in range(len(s)+1))


def get_mask_list(mask_str):
    assert isinstance(mask_str, str)
    assert len(mask_str) == 36
    mask_or = 0
    power_list = []
    power = 1
    for i in range(35, -1, -1):
        c = mask_str[i]
        if c == "1":
            mask_or = mask_or | power
        elif c == "0":
            pass
        else:
            power_list.append(power)
        power = power << 1
    global_and_mask = -1 - sum(power_list)

    mask_list = []
    for power_sublist in powerset(power_list):
        m = mask_or
        for p in power_sublist:
            m = m | p
        mask_list.append(m)
    return [global_and_mask, *mask_list]


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
        commands.append((1, get_mask_list(mask_str)))
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
mask_list = []
for cmd in commands:
    if cmd[0] == 1:
        mask_list = cmd[1]
    elif cmd[0] == 2:
        addr = cmd[1]
        value = cmd[2]
        m_and = mask_list[0]
        for m in mask_list[1:]:
            new_addr = (addr & m_and) | m
            mem[new_addr] = value
    else:
        assert False

# *** Print Answer ***

total = 0
for addr in mem:
    total += mem[addr]
print(f"Answer: {total}")

