import math

with open("day3input.txt") as tree_map:
    tree_map_list = tree_map.read().splitlines()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # (right, down)

trees_hit = 0
list_of_trees_hit = []
position_right = 0
position_down = 0

for slope in slopes:
    trees_hit = 0
    position_right = slope[0]
    position_right_orig = slope[0]
    position_down = slope[1]

    for line in tree_map_list[position_down::position_down]:
        while position_right >= len(line):
            line += line
        if line[position_right] == '#':
            trees_hit += 1
        position_right += position_right_orig
    list_of_trees_hit.append(trees_hit)

product_of_trees_hit = math.prod(list_of_trees_hit)

print(product_of_trees_hit)
