input_file = open('inputs/d11.txt', 'r')
seat_map = input_file.read().splitlines()

import time

padded_seat_map = []
padded_seat_map.append(['N']*(len(seat_map[0])+2))
for row in seat_map:
  row_as_list = []
  row_as_list[:0] = row
  row_as_list.insert(0,'N')
  row_as_list.append('N')
  padded_seat_map.append(row_as_list)
padded_seat_map.append(['N']*(len(seat_map[0])+2))

def get_neighbours_part1(map, i, j):
  neighbours = []
  for k in range(-1, 2):
    for l in range(-1, 2):
      if not (k == 0 and l == 0):
        neighbours.append(map[i + k][j + l])
  return neighbours

# part1
t0 = time.time()
next_iter = [padded_seat_map[x].copy() for x in range(len(padded_seat_map))]
prev_iter = [padded_seat_map[x].copy() for x in range(len(padded_seat_map))]
change_recorded = True
while change_recorded:
  change_recorded = False
  for i in range(1, len(padded_seat_map)-1):
    for j in range(1, len(padded_seat_map[0])-1):
      neigh = get_neighbours_part1(prev_iter, i, j)
      if prev_iter[i][j] == 'L':
        if neigh.count('#') == 0:
          change_recorded = True
          next_iter[i][j] = '#'
      elif prev_iter[i][j] == '#':
        if neigh.count('#') >= 4:
          change_recorded = True
          next_iter[i][j] = 'L'
  prev_iter = [next_iter[x].copy() for x in range(len(padded_seat_map))]

num_occupied = 0
for row in prev_iter:
  num_occupied += row.count('#')
t1 = time.time()
print(num_occupied)
print((t1-t0)*1000, ' ms')

def get_neighbours_part2(map, i, j):
  vecs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
  neighbours = []
  for vec in vecs:
    cont = True
    k = i + vec[0]
    l = j + vec[1]
    while cont and map[k][l] != 'N':
      if map[k][l] == 'L' or map[k][l] == '#':
        cont = False
        neighbours.append(map[k][l])
      k += vec[0]
      l += vec[1]
  return neighbours

# part 2
t0 = time.time()
next_iter = [padded_seat_map[x].copy() for x in range(len(padded_seat_map))]
prev_iter = [padded_seat_map[x].copy() for x in range(len(padded_seat_map))]
change_recorded = True
while change_recorded:
  change_recorded = False
  for i in range(1, len(padded_seat_map)-1):
    for j in range(1, len(padded_seat_map[0])-1):
      neigh = get_neighbours_part2(prev_iter, i, j)
      if prev_iter[i][j] == 'L':
        if neigh.count('#') == 0:
          change_recorded = True
          next_iter[i][j] = '#'
      elif prev_iter[i][j] == '#':
        if neigh.count('#') >= 5:
          change_recorded = True
          next_iter[i][j] = 'L'
  prev_iter = [next_iter[x].copy() for x in range(len(padded_seat_map))]

num_occupied = 0
for row in prev_iter:
  num_occupied += row.count('#')
t1 = time.time()
print(num_occupied)
print((t1-t0)*1000, ' ms')