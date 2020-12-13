input_file = open('inputs/d13.txt', 'r')
readin = input_file.read().splitlines()

ts_init = int(readin[0])
buses =  readin[1].split(",")
buses_filt =  [int(b) for b in readin[1].split(",") if b is not 'x']

# part1
done = False
ts_iter = ts_init
while not done:
  for b in buses_filt:
    if ts_iter % b is 0:
      done = True
      print(b * (ts_iter - ts_init))
      break
  ts_iter += 1

# part2
done = False
t = 0

max_bus = max(buses_filt)
buses_inds = []
buses_filt.sort()
for b in buses_filt:
  buses_inds.append([b, buses.index(str(b))])

# TODO

# for b in buses_inds:
  # print(b)
# for i in range(len(buses_inds) -2,-1, -1):
  # print(i)


# t = int(100000000000000 /  buses_inds[-1][0]) * buses_inds[-1][0]  - buses_inds[-1][1]
# while not done:
  # done = True
  # for i in range(len(buses_inds) -2,-1, -1):
    # if (t + buses_inds[i][1]) % buses_inds[i][0] == 0:
      # continue
    # else :
      # t += buses_inds[-1][0]
      # done = False
# print(t)

    