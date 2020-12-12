input_file = open('inputs/d4.txt', 'r')
batch = input_file.read().splitlines()

import string
import time

t0 = time.time()
passports_strings = []
str_tmp = ''
for i in range(len(batch)):
  if batch[i] == '':
    passports_strings.append(str_tmp)
    str_tmp = ''
    continue
  str_tmp += batch[i] + ' '
passports_strings.append(str_tmp)
t1 = time.time()
print((t1-t0)*1000, ' ms')


class Passport():
  REQ_FIELDS =  ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

  def __init__(self, passport_str):
    self.fields = {}
    for fd in Passport.REQ_FIELDS:
      if passport_str.count(fd+':') > 0:
        self.fields[fd] = passport_str[passport_str.find(fd+':') + 4: passport_str.find(fd+':') + 4 + passport_str[passport_str.find(fd+':') + 4:].find(' ')]

  def isValidPart1(self):
    if len(self.fields) == len(Passport.REQ_FIELDS):
      return True
    else:
      return False

  def isValidPart2(self):
    if not self.isValidPart1():
      return False
    if (int(self.fields['byr']) < 1920 or int(self.fields['byr']) > 2002):
      return False
    if (int(self.fields['iyr']) < 2010 or int(self.fields['iyr']) > 2020):
      return False
    if (int(self.fields['eyr']) < 2020 or int(self.fields['eyr']) > 2030):
      return False
    if (self.fields['hgt'][-2:] == 'cm' or self.fields['hgt'][-2:] == 'in'):
      if (self.fields['hgt'][-2:] == 'cm'):
        if (int(self.fields['hgt'][:-2]) < 150 or int(self.fields['hgt'][:-2]) > 193):
          return False
      else :
        if (int(self.fields['hgt'][:-2]) < 59 or int(self.fields['hgt'][:-2]) > 76):
          return False
    else:
      return False
    if (self.fields['hcl'][0] != '#' or len(self.fields['hcl']) != 7 or any(letter in self.fields['hcl'] for letter in string.ascii_lowercase[6:])):
      return False
    if (not any(col in self.fields['ecl'] for col in ['amb','blu','brn','gry','grn','hzl','oth'])):
      return False
    if (len(self.fields['pid'] )!= 9):
      return False
    return True

# part1
t0 = time.time()
num_valid = 0
for p in passports_strings:
  if (Passport(p).isValidPart1()):
    num_valid += 1
t1 = time.time()
print(num_valid)
print((t1-t0)*1000, ' ms')

# part 2
t0 = time.time()
num_valid = 0
for p in passports_strings:
  if (Passport(p).isValidPart2()):
    num_valid += 1
t1 = time.time()
print(num_valid)
print((t1-t0)*1000, ' ms')
