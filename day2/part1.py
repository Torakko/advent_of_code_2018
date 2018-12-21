#! /usr/bin/env python

import os
import sys

data = []
with open('input', 'r') as file:
    for line in file:
       data.append(line.strip())

test = []
with open('test', 'r') as file:
    for line in file:
       line = ''.join(sorted(line.strip()))
       test.append(line)




two = 0
three = 0
for box in data:
	#print box
	count = {i:box.count(i) for i in box}
	if 2 in count.values():
		two += 1
		#print 'two'
	if 3 in count.values():
		three += 1
		#print 'three'

print two * three

