#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def transform_step(subj_num, curr_num):
    denom = 20201227
    return (subj_num * curr_num) % denom


def transform(loop_size, subj_num=7):
    curr_num = 1
    for _ in range(loop_size):
        curr_num = transform_step(subj_num, curr_num)
    return curr_num


def find_loop_size(public_key, subj_num=7):
    curr_num = 1
    loop_count = 0;
    while curr_num != public_key:
        curr_num = transform_step(subj_num, curr_num)
        loop_count += 1
    assert transform(loop_count, subj_num) == public_key
    return loop_count


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

public_keys = []
for line in sys.stdin:
    line = line.rstrip()
    try:
        public_keys.append(int(line))
    except:
        assert False, f"Input line is not integer: {line}"
assert len(public_keys) == 2
print(f"*** public_keys: {public_keys}")

# *** Do Computation ***

loop_sizes = []
loop_sizes.append(find_loop_size(public_keys[0]))
loop_sizes.append(find_loop_size(public_keys[1]))
print(f"*** loop_sizes: {loop_sizes}")
encryption_key = transform(loop_sizes[0], public_keys[1])
assert encryption_key == transform(loop_sizes[1], public_keys[0])

# *** Print Answer ***

print("-" * 60)
print(f"Answer: {encryption_key}")

