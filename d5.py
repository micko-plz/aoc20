input_file = open('/home/mcko_plz/git/aoc20/inputs/d5.txt', 'r')
seats = input_file.read().splitlines()

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
max_seatId = 0
for seat in seats:
  max_seatId = max(max_seatId, getSeatId(seat))
print(max_seatId)

# part2
seatIds = []
for seat in seats:
  seatIds.append(getSeatId(seat))
seatIds.sort()
for testId in range(seatIds[0], seatIds[-1]):
  if (seatIds.count(testId) == 0):
    if (seatIds.count(testId -1) + seatIds.count(testId + 1) == 2):
      print(testId)
      break