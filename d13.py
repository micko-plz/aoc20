input_file = open('inputs/d13.txt', 'r')
readin = input_file.read().splitlines()

import time

ts_init = int(readin[0])
buses =  readin[1].split(",")
buses_filt =  [int(b) for b in readin[1].split(",") if b is not 'x']

# part1
t0 = time.time()
done = False
ts_iter = ts_init
while not done:
  for b in buses_filt:
    if ts_iter % b is 0:
      done = True
      print(b * (ts_iter - ts_init))
      break
  ts_iter += 1
t1 = time.time()
print((t1-t0)*1000, ' ms')

# part2
# using CRT because reddit told me to :(
max_bus = max(buses_filt)
buses_inds = []
buses_filt.sort()
t0 = time.time()
N = 1
for bus in buses_filt:
  N *= bus
bi = []
Ni = []
xi = []
bNxi = 0
for i, bus in enumerate(buses_filt):
  bi.append(bus - (buses.index(str(bus)) % bus))
  Ni.append(int(N / bus))
  xt = 1
  while ((Ni[i]*xt) % bus != 1):
    xt += 1
  if xt < 0:
    xt += bus
  xi.append(xt)
  bNxi += bi[i]*Ni[i]*xi[i]

while (bNxi - N > 0):
  bNxi -= N
print(bNxi)
t1 = time.time()
print((t1-t0)*1000, ' ms')
