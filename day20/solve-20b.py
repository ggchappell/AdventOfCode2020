#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search
import itertools    # .product


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# is_square_image: return True if image is an array of strings of all
# the same length, len(image) is the same as this length, and this
# length is not zero. Return False otherwise.
def is_square_image(image):
    if not isinstance(image, list):
        return False
    size = len(image)
    if size == 0:
        return False
    for row in image:
        if not isinstance(row, str):
            return False
        if not len(row) == size:
            return False
    return True


# A side_num is:
#   0: top
#   1: right
#   2: bottom
#   3: left
# A side is returned as a string, entries in clockwise order (so bottom
# & left sides get reversed).
def get_side(tile, side_num):
    assert is_square_image(tile)
    assert len(tile) == tile_size
    if side_num == 0:    # top
        s = tile[0]
        return s
    elif side_num == 1:  # right
        s = ""
        for row in tile:
            s += row[-1]
        return s
    elif side_num == 2:  # bottom
        s = tile[-1][::-1]  # Last row, reversed
        return s
    elif side_num == 3:  # left
        s = ""
        for row in tile:
            s = row[0] + s
        return s
    else:
        assert False, f"Bad side_num: {side_num}"


# rotate_ccw: given image, return it rotated 90 degrees ccw.
# Does not modify original.
def rotate_ccw(image):
    assert is_square_image(image)
    size = len(image)
    new_image = [""]*size
    for row in image:
        for i, c in enumerate(row):
            new_image[size-1-i] += c
    return new_image


# flop: given image, return it flopped (horizontal)
# Does not modify original.
def flop(image):
    assert is_square_image(image)
    new_image = []
    for row in image:
        new_image.append(row[::-1])  # row reversed
    return new_image


# advance: given (x, y), return is advanced in given direction: 0-3
def advance(loc, side_num):
    x, y = loc
    if side_num == 0:
        return (x, y-1)
    elif side_num == 1:
        return (x+1, y)
    elif side_num == 2:
        return (x, y+1)
    elif side_num == 3:
        return (x-1, y)
    else:
        assert False, f"Bad side_num: {side_num}"


# file_tile: given tiles (dict), side_num, and side (str), attempts to
# find a tile that matches up with the given side. If not found, returns
# (False, None, None). If found, removes tile from tiles and returns the
# tile rotated/flipped, as (True, tile_number, transformed_tile).
def find_tile(tiles, side_num, side):
    assert isinstance(tiles, dict)
    assert isinstance(side_num, int)
    assert 0 <= side_num < 4
    assert isinstance(side, str)
    assert len(side) == tile_size

    side_rev = side[::-1]  # side reversed
    for tn2 in tiles:
        tile2 = tiles[tn2]
        for side_num2 in range(4):
            side2 = get_side(tile2, side_num2)
            if side2 == side or side2 == side_rev:
                rev_flag = side2 == side_rev
                for i in range(side_num2):
                    tile2 = rotate_ccw(tile2)
                if not rev_flag:
                    tile2 = flop(tile2)
                for i in range((6-side_num)%4):
                    tile2 = rotate_ccw(tile2)
                del tiles[tn2]
                return (True, tn2, tile2)
    return (False, None, None)


# mark_sea_monsters: for each sea monster in the given image, as
# currently oriented, change each "#" to "O". Sea monsters consist of
# "#" and "O" characters. Modifies given image.
def mark_sea_monsters(image):
    assert is_square_image(image)
    size = len(image)
    sm = [
           "..................#.",
           "#....##....##....###",
           ".#..#..#..#..#..#...",
         ]
    sm_height = len(sm)
    sm_width = len(sm[0])
    for x, y in itertools.product(range(size+1-sm_width),
                                  range(size+1-sm_height)):
        for smx, smy in itertools.product(range(sm_width),
                                          range(sm_height)):
            if sm[smy][smx] != "#":
                continue
            c = image[y+smy][x+smx]
            if c != "#" and c != "O":
                break
        else:
            for smx, smy in itertools.product(range(sm_width),
                                              range(sm_height)):
                if sm[smy][smx] != "#":
                    continue
                image[y+smy] = (
                    image[y+smy][:x+smx] + "O" + image[y+smy][x+smx+1:])
            

# ======================================================================
# MAIN PROGRAM(
# ======================================================================


# *** Process Input ***

tile_size = 10

tiles = {}
curr_tile_num = -1
curr_tile = []
for line in sys.stdin:
    line = line.rstrip()
    if not line:
        assert curr_tile_num != -1
        assert len(curr_tile) == tile_size
        assert curr_tile_num not in tiles
        tiles[curr_tile_num] = curr_tile
        curr_tile_num = -1
        curr_tile = []
    else:
        mo1 = re.search(r"^Tile (\d{4}):$", line)
        if mo1:
            assert curr_tile_num == -1
            assert curr_tile == []
            curr_tile_num = int(mo1[1])
        else:
            assert curr_tile_num != -1
            assert len(curr_tile) < tile_size
            assert len(line) == tile_size
            curr_tile.append(line)
if curr_tile_num != -1:
    assert len(curr_tile) == tile_size
    assert curr_tile_num not in tiles
    tiles[curr_tile_num] = curr_tile

# *** Do Computation ***

# Get a tile
for ftn in tiles:
    break
first_tile = tiles[ftn]
# Remove it from master list
del tiles[ftn]
# Add to puzzle & do a DFS
todo = []
puzzle_tiles = {}
puzzle_tns = {}
todo.append((0,0))
puzzle_tiles[(0,0)] = first_tile
puzzle_tns[(0,0)] = ftn
min_x = 0
max_x = 0
min_y = 0
max_y = 0
while todo:
    curr_loc = todo.pop()
    for side_num in range(4):
        new_loc = advance(curr_loc, side_num)
        if new_loc in puzzle_tiles:
            continue
        side = get_side(puzzle_tiles[curr_loc], side_num)
        success, tn, tile = find_tile(tiles, side_num, side)
        if not success:
            continue
        puzzle_tiles[new_loc] = tile
        puzzle_tns[new_loc] = tn
        todo.append(new_loc)
        min_x = min(min_x, new_loc[0])
        max_x = max(max_x, new_loc[0])
        min_y = min(min_y, new_loc[1])
        max_y = max(max_y, new_loc[1])

# Make stitched-together image
image = []
for y in range(min_y, 1+max_y):
    assert tile_size >= 3
    for _ in range(tile_size-2):
        image.append("")
    for x in range(min_x, 1+max_x):
        for i in range(tile_size-2):
            s = puzzle_tiles[(x, y)][i+1][1:-1]
            image[i+2-tile_size] += s

# Mark all sea monsters
mark_sea_monsters(image)
for _ in range(3):
    image = rotate_ccw(image)
    mark_sea_monsters(image)
image = flop(image)
mark_sea_monsters(image)
for _ in range(3):
    image = rotate_ccw(image)
    mark_sea_monsters(image)

# *** Print Answer ***

result = 0
for row in image:
    for c in row:
        if c == "#":
            result += 1
print(f"Answer: {result}")

