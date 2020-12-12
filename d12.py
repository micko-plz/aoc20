input_file = open('inputs/d12.txt', 'r')
instructions = input_file.read().splitlines()

import time
from math import cos, sin, radians

# part1
t0 = time.time()
init = [0,0,0]
for instr in instructions:
  if instr[0] == 'N':
    init[0] += int(instr[1:])
  elif instr[0] == 'S':
    init[0] -= int(instr[1:])
  elif instr[0] == 'E':
    init[1] += int(instr[1:])
  elif instr[0] == 'W':
    init[1] -= int(instr[1:])
  elif instr[0] == 'L':
    init[2] += radians(int(instr[1:]))
  elif instr[0] == 'R':
    init[2] -= radians(int(instr[1:]))
  elif instr[0] == 'F':
    init[0] +=  int(sin(init[2]) * int(instr[1:]))
    init[1] +=  int(cos(init[2]) * int(instr[1:]))
print(abs(init[0]) + abs(init[1]))
t1 = time.time()
print((t1-t0)*1000, ' ms')

# part2
t0 = time.time()
init_wpt = [1, 10]
init = [0, 0, 0]
for instr in instructions:
  if instr[0] == 'N':
    init_wpt[0] += int(instr[1:])
  elif instr[0] == 'S':
    init_wpt[0] -= int(instr[1:])
  elif instr[0] == 'E':
    init_wpt[1] += int(instr[1:])
  elif instr[0] == 'W':
    init_wpt[1] -= int(instr[1:])
  elif instr[0] == 'L':
    before = init_wpt.copy()
    init_wpt[0] = int(sin(radians(int(instr[1:]))) * before[1]) + int(cos(radians(int(instr[1:]))) * before[0])
    init_wpt[1] = int(-sin(radians(int(instr[1:]))) * before[0]) + int(cos(radians(int(instr[1:]))) * before[1])
  elif instr[0] == 'R':
    before = init_wpt.copy()
    init_wpt[0] = int(sin(radians(-int(instr[1:]))) * before[1])+ int(cos(radians(-int(instr[1:]))) * before[0])
    init_wpt[1] = int(-sin(radians(-int(instr[1:]))) * before[0]) + int(cos(radians(-int(instr[1:]))) * before[1])
  elif instr[0] == 'F':
    init[0] +=  init_wpt[0] * int(instr[1:])
    init[1] +=  init_wpt[1] * int(instr[1:])
print(abs(init[0]) + abs(init[1]))
t1 = time.time()
print((t1-t0)*1000, ' ms')