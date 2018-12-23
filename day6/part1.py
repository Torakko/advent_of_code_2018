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
    #1 parse
    for line in data:
        x, y = parse(line)
        coordinates.append((x,y))

    #2 init matrix
    size = 350
    matrix = [[-1 for x in range(size)] for y in range(size)]

    #3 Put manhattan in matrix
    for j in range(size):
        for i in range(size):
            min_dist = size
            min_coord = []
            for c in range(len(coordinates)):
                x,y = coordinates[c]
                manhattan = abs(i-x) + abs(j-y)
                if manhattan < min_dist:
                    min_dist = manhattan
                    min_coord = [c]
                elif manhattan == min_dist:
                    min_coord.append(c)
            if len(min_coord) == 1:
                matrix[j][i] = min_coord[0]
            else:
                matrix[j][i] = -1


    #lines = [str(line) for line in matrix]
    #print'\n'.join(lines)
    
    #4 count number of closest positions in matrix and edge
    infinite_disqualified = []
    coord_count = [0 for x in range(len(coordinates))]
    for j in range(size):
        for i in range(size):
            value = matrix[j][i]
            if value == -1:
                continue
            coord_count[value] += 1
            if i in [0, size-1] or j in [0, size-1]:
                infinite_disqualified.append(value)

    #5 remove disqualified
    for dis in set(infinite_disqualified):
        coord_count[dis] = 0

    #print set(infinite_disqualified)
    #print coord_count
    #print "[a,  b,  c,  d,  e,  f]"
    
    return max(coord_count)
    

(real_data, test_data) = load()
print main(real_data)

