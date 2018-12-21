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
    return sp[0].strip(), sp[1].strip()

###########################################################





def main(data):
    for line in data:
        x, y = parse(line)
        print x + ', ' + y



    return '' 


(real_data, test_data) = load()
print main(test_data)

