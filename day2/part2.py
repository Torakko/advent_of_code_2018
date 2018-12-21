#! /usr/bin/env python

import os
import sys


data = []
test = []
def load():
	with open('input', 'r') as file:
		for line in file:
			data.append(line.strip())
	with open('test2', 'r') as file:
		for line in file:
			test.append(line.strip())


def check(box1, box2):
	matches = []
	misses = []
	i = 0
	for char in box1:
		if box1[i] == box2[i]:
			matches.append(box1[i])
		else:
			misses.append(box1[i])
		i += 1
	#print "({} {} {})".format(box1, box2, matches)
	if len(misses) > 1:
		return False
	else:
		return ''.join(matches)


def main(inbox):
	boxes = []
	for new_box in inbox:
		for old_box in boxes:
			res = check(new_box, old_box)
			if res:
				return res
		boxes.append(new_box)
	return 'FAILED!'


load()
print main(data)

