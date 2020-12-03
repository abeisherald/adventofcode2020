with open("day3input.txt") as tree_map:
    tree_map_list = tree_map.read().splitlines()

trees_hit = 0
position = 0

for line in tree_map_list[1:]:
    position += 3
    while position > len(line):
        line += line
    if line[position] == '#':
        trees_hit += 1

print(trees_hit)
