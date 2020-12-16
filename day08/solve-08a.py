#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def co_execute(prog):
    acc = 0
    pc = 0
    while True:
        assert 0 <= pc < len(prog)
        yield pc, acc
        opcode, arg = prog[pc]
        if opcode == "acc":
            acc += arg
            pc += 1
        elif opcode == "jmp":
            pc += arg
        elif opcode == "nop":
            pc += 1
        else:
            assert False


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

prog = []
for line in sys.stdin:
    line = line.rstrip()
    mo1 = re.search(r"^([a-z]{3}) ([\+\-]\d+)$", line)
    assert mo1
    opcode = mo1[1]
    assert opcode in { "acc", "jmp", "nop" }
    arg = int(mo1[2])
    prog.append((opcode, arg))

# *** Do Computation ***

executed = set()
for pc, acc in co_execute(prog):
    if pc in executed:
        result = acc
        break
    executed.add(pc)

# *** Print Answer ***

print(f"Answer: {result}")

