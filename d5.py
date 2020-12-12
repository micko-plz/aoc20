input_file = open('inputs/d5.txt', 'r')
seats = input_file.read().splitlines()

import time

def getSeatId(seat):
  row = 0
  col = 0

  bounds = [0,128]
  for i in range(0,6):
    if seat[i] == 'F':
      bounds[1] -= (bounds[1] - bounds[0])/2
    else :
      bounds[0] += (bounds[1] - bounds[0])/2
  row = int(bounds[0]) if (seat[6] == 'F') else int(bounds[1]) -1

  bounds = [0,8]
  for i in range(7, 9):
    if seat[i] == 'L':
      bounds[1] -= (bounds[1] - bounds[0])/2
    else :
      bounds[0] += (bounds[1] - bounds[0])/2
  col = int(bounds[0]) if (seat[9] == 'L') else int(bounds[1]) -1

  seatId = row * 8 + col
  return seatId

# part1
t0 = time.time()
max_seatId = 0
for seat in seats:
  max_seatId = max(max_seatId, getSeatId(seat))
t1 = time.time()
print(max_seatId)
print((t1-t0)*1000, ' ms')

# part2
t0 = time.time()
seatIds = []
for seat in seats:
  seatIds.append(getSeatId(seat))
seatIds.sort()
for testId in range(seatIds[0], seatIds[-1]):
  if (seatIds.count(testId) == 0):
    if (seatIds.count(testId -1) + seatIds.count(testId + 1) == 2):
      print(testId)
      t1 = time.time()
      break
print((t1-t0)*1000, ' ms')