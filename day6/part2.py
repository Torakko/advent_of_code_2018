#! /usr/bin/env python

import os
import sys

def load():
    real = []
    with open('real', 'r') as file:
        for line in file:
            real.append(line.strip())
    test = []
    with open('test', 'r') as file:
        for line in file:
            test.append(line.strip())
    return real, test

###########################################################

#import re
#
#def parse(line):
#    match = re.match("^\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)$", line)
#    Y = int(match.group(1))
#    M = int(match.group(2))
#    D = int(match.group(3))
#    h = int(match.group(4))
#    m = int(match.group(5))
#    message = match.group(6)
#    return Y, M, D, h, m, message

def parse(line):
    sp = line.split(',')
    return int(sp[0].strip()), int(sp[1].strip())

###########################################################





def main(data):
    coordinates = []
    for line in data:
        x, y = parse(line)
        coordinates.append((x,y))

    size = 350
    area = 0
    for j in range(size):
        for i in range(size):
            manhattan = 0
            for c in range(len(coordinates)):
                x,y = coordinates[c]
                manhattan += abs(i-x) + abs(j-y)
            if manhattan < 10000:
                area += 1
    return area

    

(real_data, test_data) = load()
print main(real_data)

