input_file = open('/home/michael/git/PersonalStuff/aoc20/inputs/d10.txt', 'r')

import time

ints = [int(line) for line in input_file.read().splitlines()]
ints.sort()

# part1
t0 = time.time()
ints.append(ints[-1] + 3)
current = 0
num_1 = 0
num_3 = 0
for val in ints:
  if (val - current) == 1:
    num_1 += 1
  elif (val - current) == 3:
    num_3 += 1
  current = val
t1 = time.time()
print(num_1 * num_3)
print((t1-t0)*1000, ' ms')

# part2
ints.insert(0, 0)

import numpy as np

def get_parents(ind):
  parents = []
  ind_c = ind + 1
  while ind_c < len(ints) and ints[ind_c] - ints[ind] < 4:
      parents.append(ind_c)
      ind_c += 1
  return parents

num_ada = len(ints)
A = np.zeros((num_ada, num_ada), dtype=np.int32)
for i in range(num_ada):
  A[i, get_parents(i)] = 1
  
t0 = time.time()
print(int(np.linalg.inv(np.identity(num_ada, dtype=np.int32) - A)[0, -1]))
t1 = time.time()
print((t1-t0)*1000, ' ms')