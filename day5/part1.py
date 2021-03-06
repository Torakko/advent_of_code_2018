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

import re

def parse(line):
    match = re.match("^\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)$", line)
    Y = int(match.group(1))
    M = int(match.group(2))
    D = int(match.group(3))
    h = int(match.group(4))
    m = int(match.group(5))
    message = match.group(6)
    return Y, M, D, h, m, message

###########################################################

def check(a, b):
    return abs(ord(a)-ord(b)) == 32


def reduce_polymer(a, b):
    #print a
    #print b
    #print '-------------------'
    if a == '':
        return b
    if abs(ord(a[-1])-ord(b)) == 32:
        return a[:-1]
    else:
        return a + b

def main(data):
    old_len = len(data)

    #print reduce(reduce_polymer, 'baABCCc')
    #return ''

    while True:
        data = reduce(reduce_polymer, data)
        new_len = len(data)
        #print "{} {}".format(new_len, data)
        if old_len == new_len:
            return new_len
        old_len = new_len


(real, test) = load()
print main(real)

