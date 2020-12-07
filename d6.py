input_file = open('/home/mcko_plz/git/aoc20/inputs/d6.txt', 'r')
lines = input_file.read().splitlines()

import string
import time

t0 = time.time()
groups = []
str_tmp = ''
for i in range(len(lines)):
  if lines[i] == '':
    groups.append(str_tmp)
    str_tmp = ''
    continue
  str_tmp += lines[i] + ' '
groups.append(str_tmp)
t1 = time.time()
print((t1-t0)*1000, ' ms')

# part1
t0 = time.time()
counts_total = 0
counts_per_group = 0 
for group in groups:
  for char in string.ascii_lowercase:
    if group.count(char) > 0:
      counts_per_group += 1
  counts_total += counts_per_group
  counts_per_group = 0
t1 = time.time()
print(counts_total)
print((t1-t0)*1000, ' ms')

# part2
t0 = time.time()
counts_total = 0
counts_per_group = 0 
for group in groups:
  asList = group[:-1].split(' ')
  for char in string.ascii_lowercase:
    isPresent = True
    for vote in asList:
      if vote.count(char) == 0:
        isPresent = False
    if isPresent:
      counts_per_group+=1
  counts_total+= counts_per_group
  counts_per_group =0
t1 = time.time()
print(counts_total)
print((t1-t0)*1000, ' ms')

