input_file = open('/home/mcko_plz/git/aoc20/inputs/d2.txt', 'r')
inputs = input_file.read().splitlines()

class Entry():
  def __init__(self, string):
    self.min = int(string[:string.find('-')])
    self.max = int(string[string.find('-')+1:string.find(' ')])
    self.char = string[string.find(':')-1]
    self.pw = string[string.rfind(' ')+1:]

  def isValidPart1(self):
    if (self.min <=self.pw.count(self.char) <= self.max):
      return True
    else:
      return False

  def isValidPart2(self):
    if ((self.pw[self.min-1] == self.char) == (self.pw[self.max-1] == self.char)):
      return False
    else:
      return True      

entries = [Entry(line) for line in inputs]

# part1
num_valid = 0
for ent in entries:
  if ent.isValidPart1():
    num_valid += 1
print(num_valid)

# part2
num_valid = 0
for ent in entries:
  if ent.isValidPart2():
    num_valid += 1
print(num_valid)