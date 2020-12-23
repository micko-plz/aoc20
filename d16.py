input_file = open('inputs/d16.txt', 'r')
readin = input_file.read().splitlines()

import time

# parse
t0 = time.time()
classes = {}
i = 0
while (readin[i]!=''):
  class_name = readin[i][:readin[i].find(':')]
  classes[class_name] = []
  classes[class_name].append(range(int(readin[i][readin[i].find(':')+2:readin[i].find('-')]), int(readin[i][readin[i].find('-')+1:readin[i].find('or ')-1]) + 1))
  classes[class_name].append(range(int(readin[i][readin[i].find('or ')+3:-4]), int(readin[i][-3:])+1))
  i += 1
i+=2
my_ticket = [int(val) for val in readin[i].split(',')]
i+=3
nearby_tickets = []
while (i < len(readin)):
  nearby_tickets.append([int(val) for val in readin[i].split(',')])
  i += 1
t1 = time.time()
print((t1-t0)*1000, ' ms')

# part1
t0 = time.time()
error = 0
nearby_tickets_red = nearby_tickets.copy()
for i, t in enumerate(nearby_tickets):
  for num in t:
    isValid = False
    for vals in classes.values():
      for val in vals:
        if num in val:
          isValid = True
    if not isValid:
      error += num
      nearby_tickets_red.remove(t) # for part2
t1 = time.time()
print(error)
print((t1-t0)*1000, ' ms')

# part2
t0 = time.time()
possible_ordering = classes.copy()
for k in possible_ordering.keys():
  possible_ordering[k] = []

for c in classes.keys():
  for o in range(len(classes)):
    isValid = True
    for t in nearby_tickets_red:
      if not (t[o] in classes[c][0] or t[o] in classes[c][1]):
        isValid = False
        break
    if isValid:
      possible_ordering[c].append(o)

done = False
done_list = []
while not done:
  for c in possible_ordering.keys():
    val_to_remove = -1
    if len(possible_ordering[c]) == 1 and c not in done_list:
      val_to_remove = possible_ordering[c][0]
      done_list.append(c)
      break

  done = True
  for cl in possible_ordering.keys():
    if not cl == c and possible_ordering[cl].count(val_to_remove):
      possible_ordering[cl].remove(val_to_remove)
    if not len(possible_ordering[cl]) == 1:
      done = False

ans = 1
for c in possible_ordering.keys():
  if c.count('departure'):
    ans *= my_ticket[possible_ordering[c][0]]
t1 = time.time()
print(ans)
print((t1-t0)*1000, ' ms')





