#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 Code Jam Qualification round
    Problem-A: Oversized Pancake
'''
import sys


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: Test Case
        Update: Pacake status, Flipper size
        Return: None
    '''

    x, y = sys.stdin.readline().split()
    tc.pancake = list(x)
    tc.flip_size = int(y)

    return


def flip_cake(pancake, pos, flip_size):
    '''
        Input List: pancake
        Input Integer: pos
        Input Integer: flip_size
        Update : pancake (Flip '+' and '-')
        Return: None
    '''

    for i in range(flip_size):
        if pancake[i+pos] == '-':
            pancake[i+pos] = '+'
        else:
            pancake[i+pos] = '-'

    return

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    len_pancake = len(tc.pancake)
    pos = 0
    flip_count = 0

    while pos <= len_pancake - tc.flip_size:
        if tc.pancake[pos] != '+':
            flip_cake(tc.pancake, pos, tc.flip_size)
            flip_count += 1
        pos += 1

    while pos != len_pancake:
        if tc.pancake[pos] != '+':
            print('IMPOSSIBLE')
            return
        pos += 1

    print(flip_count)
    return


##
##  Main routine
##
if __name__ == '__main__':

    tc = TestCase()
    tc.t = int(sys.stdin.readline())

    for i in range(tc.t):
        print('Case #', i+1, ': ', sep='', end='')
        solve(tc)
