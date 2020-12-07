input_file = open('/home/mcko_plz/git/aoc20/inputs/d3.txt', 'r')
world_map = input_file.read().splitlines()

import time

map_width = len(world_map[0])
map_length = len(world_map)

def num_trees(right, down):
  pos = [0,0]
  num_trees = 0
  while (pos[0] < map_length):
    if (world_map[pos[0]][pos[1]] == '#'):
      num_trees += 1
    pos[0] += down
    pos[1] = pos[1] + right if (pos[1] + right < map_width) else (right - map_width + pos[1])
  return num_trees


# part1
t0 = time.time()
print(num_trees(3, 1))
t1 = time.time()
print((t1-t0)*1000, ' ms')

# part2
t0 = time.time()
print(num_trees(1, 1) * num_trees(3, 1) * num_trees(5, 1) * num_trees(7, 1) * num_trees(1, 2))
t1 = time.time()
print((t1-t0)*1000, ' ms')