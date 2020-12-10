input_file = open('inputs/d1.txt', 'r')
ints = [int(line) for line in input_file.readlines()]

import time

# part1 
t0 = time.time()
for i, val in enumerate(ints):
  if (2020 - val) in ints[i:]:
    print(val * (2020 - val))
    t1 = time.time()
    break
print((t1-t0)*1000, ' ms')

# part2
t0 = time.time()
for i, val1 in enumerate(ints):
  for j, val2 in enumerate(ints[i:]):
    if (2020 - val1 - val2) in ints[j:]:
      print(val1 * val2 * (2020 - val1 - val2))
      t1 = time.time()
      break
  else:
    continue
  break
print((t1-t0)*1000, ' ms')