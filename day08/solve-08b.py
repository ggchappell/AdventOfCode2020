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
        yield pc, acc
        if pc == len(prog):
            return
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

def try_modified_prog(prog, index):
    if prog[index][0] not in { "jmp", "nop" }:
        return (0, None)

    new_prog = prog.copy()
    if new_prog[index][0] == "jmp":
        new_prog[index] = ("nop", new_prog[index][1])
    else:
        new_prog[index] = ("jmp", new_prog[index][1])

    executed = set()
    for pc, acc in co_execute(new_prog):
        if pc in executed:
            return (1, None)
        executed.add(pc)
    return (2, acc)


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

for i in range(len(prog)):
    code, result = try_modified_prog(prog, i)
    if code == 2:
        break

# *** Print Answer ***

print(f"Answer: {result}")

