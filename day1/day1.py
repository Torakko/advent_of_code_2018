#! /usr/bin/env python

import os

sum = 0
with open('input', 'r') as file:
    for line in file:
       sum += int(line.strip())
print sum       
