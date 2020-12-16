#!/usr/bin/env python3
"""Python 3.* Quick Reference"""

# Useful docs pages

# Built-In Functions:
#   https://docs.python.org/3/library/functions.html

# Built-In Types:
#   https://docs.python.org/3/library/stdtypes.html


import sys          # .stdin

line = sys.stdin.readline()  # Read single line from std input
for line in sys.stdin:       # Read each line from stdin, includes \n

    # Strings (type str)
    print(ord(line[-1]))
    line = line.rstrip()     # Elim whitespace on right
    line = line.lstrip()     # Elim whitespace on left
    line = line.lower()      # Convert to lower-case
    print(len(line))         # Length of string
    if line:                 # Non-empty strings are truthy
        x = ord(line[0])     # Unicode codepoint
        print(chr(x))        # code -> character (type = str)

# Sets (type set)
ss = { 22, 33 }
ss.add(44)                   # Insert in set
ss.remove(44)                # Delete from set
ss.pop()                     # Remove & return an arbitrary element
ss2 = { 33, 44 }
ss3 = ss | ss2               # Union
ss3 = ss & ss2               # Intersection
ss3 = ss - ss2               # Difference
ss3 = ss ^ ss2               # Symmetric difference
                             # Above 4: assignment versions also work:
                             #   |=  &=  -=  ^=

# Lists (type list)
ll = [22, 33]
ll.append(44)                # Add to end of list
ll.pop()                     # Delete from end of list
ll.insert(0, 11)             # Add to beginning of list
ll.pop(0)                    # Delete from beginning of list
ll2 = [55, 66]
ll3 = ll + ll2               # List concatenation
ll4 = [1, 2, *ll3, 9]        # List unpacking

# F-Strings
a, b = 1, 2
print(f"ll[a] + b = {ll[a]+b}")

