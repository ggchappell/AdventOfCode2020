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

counts = [0] * len(nums)
counts[0] = 1
for i in range(1, len(nums)):
    k = i-1
    while k >= 0 and nums[i]-nums[k] <= 3:
        counts[i] += counts[k]
        k -= 1

# *** Print Answer ***

print(f"Answer: {counts[-1]}")

