input_file = open('/home/michael/git/PersonalStuff/aoc20/inputs/d8.txt', 'r')
lines = input_file.read().splitlines()

import time

# part1
t0 = time.time()
line_visited = [0]*len(lines)
i = 0
acc = 0
while line_visited[i] != 1:
  if lines[i][:3] == 'acc':
    line_visited[i] += 1
    acc += int(lines[i][lines[i].rfind(' ')+1:])
    i += 1
  elif lines[i][:3] == 'jmp':
    line_visited[i] += 1
    i += int(lines[i][lines[i].rfind(' ')+1:])
  elif lines[i][:3] == 'nop':
    line_visited[i] += 1
    i += 1
t1 = time.time()
print(acc)
print((t1-t0)*1000, ' ms')

# part2
t0 = time.time()
lines_original = lines.copy()
for ind in range(len(lines)):
  line_visited = [0]*len(lines)
  i = 0
  acc = 0
  while line_visited[i] != 1:
    if lines[i][:3] == 'acc':
      line_visited[i] += 1
      acc += int(lines[i][lines[i].rfind(' ')+1:])
      i += 1
    elif lines[i][:3] == 'jmp':
      line_visited[i] += 1
      i += int(lines[i][lines[i].rfind(' ')+1:])
    elif lines[i][:3] == 'nop':
      line_visited[i] += 1
      i += 1
    if (i == len(lines)):
      print(acc)
      line_visited[i-1] = 1
      ind = len(lines) -1
      break
  lines = lines_original.copy()
  if lines[ind][:3] == 'jmp':
    lines[ind] = 'nop' + lines[ind][3:]
    continue 
  if lines[ind][:3] == 'nop':
    lines[ind] = 'jmp' + lines[ind][3:]
t1 = time.time()
print((t1-t0)*1000, ' ms')