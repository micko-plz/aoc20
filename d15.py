input_file = open('inputs/d15.txt', 'r')
readin = input_file.read().splitlines()
ints = [int(i) for i in readin[0].split(',')]

import time

def doIt(num):
  spoken = {}
  
  last_spoken = ints[0]
  for i, val in enumerate(ints):
    if not val in spoken.keys():
      spoken[val] = []
    spoken[val].append(i+1)
    last_spoken = val

  i+=1
  while (i < num):
    last_spoken = 0 if len(spoken[last_spoken]) == 1 else spoken[last_spoken][-1] - spoken[last_spoken][-2]
    if not last_spoken in spoken.keys():
      spoken[last_spoken] = []
    spoken[last_spoken].append(i+1)
    if len(spoken[last_spoken]) > 2:
      spoken[last_spoken].pop(0)
    i+=1

  return last_spoken

# part1
t0 = time.time()
print(doIt(2020))
t1 = time.time()
print((t1-t0)*1000, ' ms')

# part2
t0 = time.time()
print(doIt(30000000))
t1 = time.time()
print((t1-t0)*1000, ' ms')
