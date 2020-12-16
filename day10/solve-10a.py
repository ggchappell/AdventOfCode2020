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

nums = []
for line in sys.stdin:
    line = line.rstrip()
    num = int(line)
    nums.append(num)
assert len(nums) > 0

# *** Do Computation ***

nums.sort()
nums = [0, *nums, nums[-1]+3]

diff1_count = 0
diff3_count = 0
for i in range(len(nums)-1):
    diff = nums[i+1] - nums[i]
    assert 1 <= diff <= 3
    if diff == 1:
        diff1_count += 1
    elif diff == 3:
        diff3_count += 1

# *** Print Answer ***

print(f"Answer: {diff1_count * diff3_count}")

