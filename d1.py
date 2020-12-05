input_file = open('/home/mcko_plz/git/aoc20/inputs/d1.txt', 'r')
ints = [int(line) for line in input_file.readlines()]

# part1 
for i, val in enumerate(ints):
  if (2020 - val) in ints[i:]:
    print(val * (2020 - val))
    break

# part2
for i, val1 in enumerate(ints):
  for j, val2 in enumerate(ints[i:]):
    if (2020 - val1 - val2) in ints[j:]:
      print(val1 * val2 * (2020 - val1 - val2))
      break
  else:
    continue
  break