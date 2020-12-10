input_file = open('inputs/d9.txt', 'r')

import time

ints = [int(line) for line in input_file.read().splitlines()]
def isSumOfLastN(indCurrent, N):
  ints_rel = ints[indCurrent-N:indCurrent]
  for i, val in enumerate(ints_rel):
    ints_less_current = ints_rel.copy()
    ints_less_current.pop(i)
    if -val + ints[indCurrent] in ints_less_current:
      return True 
  return False

# part1
t0 = time.time()
for i in range(25, len(ints)):
  if not isSumOfLastN(i, 25):
    ind = i
    val = ints[i]
    print(ints[i])
    break
t1 = time.time()
print((t1-t0)*1000, ' ms')

ints_p2 = ints[:ind]
def isSumofAnyN(N, val):
  for i in range(len(ints_p2) - N + 1):
    if sum(ints_p2[i:i+N]) == val:
      return i
  return -1

# part2
t0 = time.time()
for N in range(len(ints_p2)):
  ret = isSumofAnyN(N, val)
  if ret > -1:
    print(min(ints_p2[ret:ret+N]) + max(ints_p2[ret:ret+N]))
    break
t1 = time.time()
print((t1-t0)*1000, ' ms')