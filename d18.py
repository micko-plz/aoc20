input_file = open('inputs/d18.txt', 'r')
lines = input_file.read().splitlines()

import time

def parse(string):
  nums, ops = [], []
  last_op_ind = -1
  for i, char in enumerate(string):
    if not char.isnumeric():
      nums.append(int(string[last_op_ind+1:i]))
      ops.append(char)
      last_op_ind = i
  nums.append(int(string[last_op_ind+1:]))
  return nums, ops

def eval_p1(string):
  nums, ops = parse(string)
  init = int(nums[0]) * int(nums[1]) if ops[0] == '*' else int(nums[0]) + int(nums[1])
  for i in range(1, len(ops)):
    init = init * nums[i+1] if ops[i] == '*' else init + nums[i+1]
  return init

def eval_p2(string):
  nums, ops = parse(string)
  while ops.count('+') != 0:
    i = ops.index('+')
    nums.insert(i, nums[i]+nums[i+1])
    nums.pop(i+1)
    nums.pop(i+1)
    ops.pop(i)

  if len(nums) == 1:
    return nums[0]

  init = int(nums[0]) * int(nums[1])
  for i in range(1, len(ops)):
    init = init * nums[i+1]
  return init

def run(isP1, lines):
  sum = 0
  for line in lines:
    line = line.replace(' ','')
    while line.count(')') + line.count('(') != 0:
      s, e = -1, -1
      last_paren = ' '
      for i, char in enumerate(line):
        if char == '(':
          s = i
          last_paren = char 
        elif char == ')':
          e = i
          if last_paren == '(':
            line = line.replace(line[s : e+1], str(eval_p1(line[s+1 : e]))) if isP1 else line.replace(line[s : e+1], str(eval_p2(line[s+1 : e])))
          break
    line = line.replace(' ','')
    t= eval_p1(line) if isP1 else eval_p2(line)
    sum += eval_p1(line) if isP1 else eval_p2(line)
  return sum

# part1
t0 = time.time()
print(run(True, lines))
t1 = time.time()
print((t1-t0)*1000, ' ms')

# part2
t0 = time.time()
print(run(False, lines))
t1 = time.time()
print((t1-t0)*1000, ' ms')
