input_file = open('inputs/d14.txt', 'r')
readin = input_file.read().splitlines()

from itertools import product
import time

# part1
def binary_list(int):
  tmp = list(bin(int))[2:]
  return ([0]*(36-len(tmp))) + tmp

def apply_mask_p1(mask, value):
  for idx in range(36):
    if mask[idx] != 'X':
      value[idx] = mask[idx]

def as_int(bin_l):
  val = 0
  for i, lt in enumerate(bin_l):
    val += int(lt) * 2**(len(bin_l)-i-1)
  return val


t0 = time.time()
mask = 0
mem = {}
for line in readin:
  if line[1] == 'a':
    mask = list(line[7:])
  else:
    val_b = binary_list(int(line[line.find('=')+2:]))
    apply_mask_p1(mask, val_b)
    mem[line[line.find('[')+1 : line.find(']')]] = as_int(val_b)

ans = 0
for v in mem.values():
  ans += v
t1 = time.time()
print(ans)
print((t1-t0)*1000, ' ms')


# part 2
def apply_mask_p2(mask, add_o):
  add_ob = binary_list(add_o)
  numX = mask.count('X')
  com = list(product([0, 1], repeat=numX))

  adds = []
  for p in com:
    xCount = 0
    value = add_ob.copy()
    for idx in range(36):
      if mask[idx] != 'X':
        if mask[idx] != '0':
          value[idx] = mask[idx]
      else:
        value[idx] = str(p[xCount])
        xCount += 1
    adds.append(as_int(value))
  return adds

t0 = time.time()
mask = 0
mem = {}
for line in readin:
  if line[1] == 'a':
    mask = list(line[7:])
  else:
    val_b = binary_list(int(line[line.find('=')+2:]))
    addst = apply_mask_p2(mask, int(line[line.find('[')+1 : line.find(']')]))
    for a in addst:
      mem[a] = int(line[line.find('=')+2:])

ans = 0
for v in mem.values():
  ans += v
t1 = time.time()
print(ans)
print((t1-t0)*1000, ' ms')