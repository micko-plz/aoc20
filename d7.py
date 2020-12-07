input_file = open('/home/mcko_plz/git/aoc20/inputs/d7.txt', 'r')
lines = input_file.read().splitlines()

class Bag():
  def __init__(self, name):
    self.name = name
    self.contains = {}
    self.total_quant = 0
    self.bags_with_this = 0

  def pushBack(self, quant, type):
    self.contains[type] = quant
    self.total_quant += quant

  def contains_total(self, all_bags):
    total = 0
    if len(self.contains) == 0:
      return total
    for bag in all_bags:
      if bag.name in self.contains:
        total += self.contains[bag.name] + self.contains[bag.name] *  bag.contains_total(all_bags)
    return total 

# read in bags
list_of_bags = []
for line in lines:
  line_as_list = line.split()
  tmp_list = []
  for i, word in enumerate(line_as_list):
    if word.count('bag') != 0:
      if (i == 2):
        bag = Bag(line_as_list[i-2] + ' ' + line_as_list[i-1])
      else:
        if not (line_as_list[i-1] == 'other'):
          bag.pushBack(int(line_as_list[i-3]), line_as_list[i-2] + ' ' + line_as_list[i-1])
  list_of_bags.append(bag)

# part1
num_bags_to_check = 0
bags_to_check = []
for bag in list_of_bags:
  if bag.name == 'shiny gold':
    bags_to_check.append(bag)

for bag_i in bags_to_check:
  for bag_t in list_of_bags:
    if bag_i.name in bag_t.contains and bags_to_check.count(bag_t) == 0:
      bags_to_check.append(bag_t)
      num_bags_to_check += 1
print(num_bags_to_check)

# part2 
for bag in list_of_bags:
  if bag.name == 'shiny gold':
    gold_bag = bag
    break
print(gold_bag.contains_total(list_of_bags))