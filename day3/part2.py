#! /usr/bin/env python

import os
import sys

real = []
test = []
def load():
    with open('data', 'r') as file:
        for line in file:
            real.append(line.strip())
    with open('test', 'r') as file:
        for line in file:
            test.append(line.strip())




class Fabric(object):
    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for x in range(size)] for y in range(size)]

    def __str__(self):
        lines = [str(line) for line in self.matrix]
        return '\n'.join(lines)

    def parse(self, indata):
        # Example: "#1 @ 1,3: 4x4"
        splitted = indata.split()
        #number = splitted[0][1:]
        offset = splitted[2].split(',')
        offset_x = int(offset[0])
        offset_y = int(offset[1][:-1])
        size = splitted[3].split('x')
        size_x = int(size[0])
        size_y = int(size[1])
                
        i_range = range(offset_x, offset_x+size_x)
        j_range = range(offset_y, offset_y+size_y)

        for j in j_range:
            for i in i_range:
                self.matrix[j][i] += 1

    # number of positions with 2 or more
    def count(self):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] > 1:
                    count += 1
        return count

    def check_all_sub_zero(self, indata):
        # Example: "#1 @ 1,3: 4x4"
        splitted = indata.split()
        number = splitted[0][1:]
        offset = splitted[2].split(',')
        offset_x = int(offset[0])
        offset_y = int(offset[1][:-1])
        size = splitted[3].split('x')
        size_x = int(size[0])
        size_y = int(size[1])
                
        i_range = range(offset_x, offset_x+size_x)
        j_range = range(offset_y, offset_y+size_y)

        res = []
        for j in j_range:
            for i in i_range:
                res.append(self.matrix[j][i] - 1)

        if all([r == 0 for r in res]):
            return number
        else:
            False


def main(inbox):
    data = real
    fabric = Fabric(1000)
    #fabric = Fabric(11)
    #fabric.parse('#123 @ 3,2: 5x4')
    for stuff in data:
        fabric.parse(stuff)
    res = False
    for stuff in data:
        res = fabric.check_all_sub_zero(stuff)
        if res:
            return res
    return 'FAILED!'


load()
print main(test)

