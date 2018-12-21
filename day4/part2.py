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

#######################################################

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


def parse_guard(message):
    return int(re.search("#(\d+)", message).group(1))


SLEEPING = '#'
AWAKE = '.'
class Guard(object):
    def __init__(self, number):
        self.number = number
        self.current_day = None
        self.current_min = None
        self.current_status = None
        self.sleep_hour_list = [0 for _ in range(60)]
        self.diary = {}

    def __str__(self):
        total = self.total_sleep()
        max_min = self.max_sleep_min()
        ans = self.number*max_min
        ret = "Guard #{}\nTotal {}\nMax min {}\nAnswer {}".format(self.number, total, max_min, ans)
        #ret = "\n{}".format(self.sleep_hour_list)
        for (no, D) in self.diary.items():
            ret += "\nDay {}: ".format(no)
            for h in D.values():
                ret += h
        return ret + '\n'

    def begin_shift(self, D):
        self.current_day = D
        self.current_min = 0
        self.current_status = AWAKE
        self.diary[D] = {}

    def fall_asleep(self, m):
        for M in range(self.current_min, m):
            self.diary[self.current_day][M] = AWAKE
        self.current_min = m
        self.current_status = SLEEPING

    def wake_up(self, m):
        for M in range(self.current_min, m):
            self.diary[self.current_day][M] = SLEEPING
            self.sleep_hour_list[M] += 1
        self.current_min = m
        self.current_status = AWAKE

    def end_shift(self):
        if self.current_status == SLEEPING:
            self.wake_up(60)
        else:
            self.fall_asleep(60)

    def total_sleep(self):
        return sum(self.sleep_hour_list)

    def max_sleep_min(self):
        max_min = None
        max_val = 0
        i = 0
        for val in self.sleep_hour_list:
            if val > max_val:
                max_val = val
                max_min = i
            i += 1
        return max_min

    def max_sleep_min_val(self):
        max_min = None
        max_val = 0
        i = 0
        for val in self.sleep_hour_list:
            if val > max_val:
                max_val = val
                max_min = i
            i += 1
        return max_val

    def answere(self):
        return self.number * self.max_sleep_min()


def total_sleep_sort(a, b):
    return b.total_sleep() - a.total_sleep()


def max_sleep_min_val_sort(a, b):
    return b.max_sleep_min_val() - a.max_sleep_min_val()


def main(data):
    data = sorted(data)
    guard_dict = {}
    current_guard = None
    current_day = 0
    for line in data:
        _Y, _M, _D, _h, m, message = parse(line)
        if 'Guard' in message:
            current_day += 1
            if current_guard:
                current_guard.end_shift()
            no = parse_guard(message)
            if no not in guard_dict:
                guard_dict[no] = Guard(no)
            current_guard = guard_dict[no]
            current_guard.begin_shift(current_day)
        elif 'wakes up' == message:
            current_guard.wake_up(m)
        elif 'falls asleep' == message:
            current_guard.fall_asleep(m)
        else:
            raise Exception(message)
            
    current_guard.end_shift()

    #guard_list = sorted(guard_dict.values(), cmp=total_sleep_sort)
    guard_list = sorted(guard_dict.values(), cmp=max_sleep_min_val_sort)
    
    return guard_list[0].answere()


(real, test) = load()
print main(real)

