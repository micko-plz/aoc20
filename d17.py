input_file = open('inputs/d17.txt', 'r')
input_slice = input_file.read().splitlines()

import time

# part1

t0 = time.time()
map_orig = {}
for y, y_row in enumerate(input_slice):
  for x, x_y in enumerate(y_row):
    map_orig[(x, y, 0)] = x_y

import itertools

increments = list(itertools.product([-1, 0, 1], repeat=3))
increments.remove((0,0,0))

def get_neighbours_p1(input):
  for coord in increments:
    yield (input[0]+coord[0], input[1]+coord[1], input[2]+coord[2])

map_new = map_orig.copy()
map_old = map_orig.copy()

def add_all_neighbours_p1(map_to_edit):
  k_orig = [k for k in map_to_edit.keys()]
  for k in k_orig:
    for n in get_neighbours_p1(k):
      if not n in map_to_edit.keys():
        map_to_edit[n] = '.' 

num_cylces = 6

while num_cylces > 0:
  map_old = map_new.copy()
  add_all_neighbours_p1(map_old)
  map_new = map_old.copy()

  for coord in map_old.keys():
    neighs = [n for n in get_neighbours_p1(coord)]
    act_c = 0
    inact_c = 0
    for n in neighs:
      if n in map_old.keys():
        if map_old[n] == '#':
          act_c += 1
        else:
          inact_c += 1
      else:
        map_new[n] = '.'
        inact_c += 1
    if map_old[coord] == '#' and act_c not in range (2, 4):
      map_new[coord] = '.'
    if map_old[coord] == '.' and act_c == 3:
      map_new[coord] = '#'
  num_cylces -= 1

ans = 0
for val in map_new.values():
  if val == '#':
    ans += 1
t1 = time.time()
print(ans)
print((t1-t0)*1000, ' ms')

# part2
t0 = time.time()
map_orig = {}
for y, y_row in enumerate(input_slice):
  for x, x_y in enumerate(y_row):
    map_orig[(x, y, 0, 0)] = x_y

increments = list(itertools.product([-1, 0, 1], repeat=4))
increments.remove((0,0,0,0))

def get_neighbours_p2(input):
  for coord in increments:
    yield (input[0]+coord[0], input[1]+coord[1], input[2]+coord[2], input[3]+coord[3])

map_new = map_orig.copy()
map_old = map_orig.copy()

def add_all_neighbours_p2(map_to_edit):
  k_orig = [k for k in map_to_edit.keys()]
  for k in k_orig:
    for n in get_neighbours_p2(k):
      if not n in map_to_edit.keys():
        map_to_edit[n] = '.' 

num_cylces = 6

while num_cylces > 0:
  map_old = map_new.copy()
  add_all_neighbours_p2(map_old)
  map_new = map_old.copy()

  for coord in map_old.keys():
    neighs = [n for n in get_neighbours_p2(coord)]
    act_c = 0
    inact_c = 0
    for n in neighs:
      if n in map_old.keys():
        if map_old[n] == '#':
          act_c += 1
        else:
          inact_c += 1
      else:
        map_new[n] = '.'
        inact_c += 1
    if map_old[coord] == '#' and act_c not in range (2, 4):
      map_new[coord] = '.'
    if map_old[coord] == '.' and act_c == 3:
      map_new[coord] = '#'
  num_cylces -= 1

ans = 0
for val in map_new.values():
  if val == '#':
    ans += 1
t1 = time.time()
print(ans)
print((t1-t0)*1000, ' ms')