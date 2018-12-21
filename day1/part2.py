#! /usr/bin/env python

import os
import sys

changes = []
with open('input', 'r') as file:
    for line in file:
       changes.append(line.strip())

sum = 0
f = []
while True:
   for change in changes:
      sum += int(change)
      if sum in f:
         print sum
         sys.exit(0)
      f.append(sum)
   print len(f)
