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
    match = re.search(" (\S+) must be finished before step (\S+) can", line)
    A = match.group(1)
    B = match.group(2)
    return A, B


###########################################################

def get_dep_dict(data):
    dep_dict = {}
    for line in data:
        depend, step = parse(line)
        if dep_dict.has_key(step):
            dep_dict[step].append(depend)
        else:
            dep_dict[step] = [depend]
        # make sure first step also is included in dict
        if not dep_dict.has_key(depend):
            dep_dict[depend] = []
    return dep_dict


def get_assembly_order(dep_dict):
    step_count = len(dep_dict)
    order = []
    while len(order) < step_count:
        possible = []
        for step, dependencies in dep_dict.items():
            if not dependencies:
                possible.append(step)
        possible = sorted(possible)
        print str(order) + ' ' + str(possible)
        next_step = possible[0]
        order.append(next_step)
        del dep_dict[next_step]
        for step_dep in dep_dict.values():
            if next_step in step_dep:
                step_dep.remove(next_step)
    return order


def main(data):
    dep_dict = get_dep_dict(data)
    order = get_assembly_order(dep_dict)
    return ''.join(order)

(real_data, test_data) = load()
print main(real_data)

