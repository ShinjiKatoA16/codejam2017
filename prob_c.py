#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 Code Jam Qualification round
    Problem-C:
'''
import sys


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: Test Case
        Update: Start Location, Delivery List
        Return: None
    '''

    tc.n, tc.k = map(int,sys.stdin.readline().split())

    return


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    stalls = {tc.n: 1}

    remain_people = tc.k

    while True:
        max_key = max(stalls)
        r_val = (max_key - 1) // 2
        l_val = (max_key - 1) - r_val
        if remain_people <= stalls[max_key]:
            break

        if r_val in stalls:
            stalls[r_val] += stalls[max_key]
        else:
            stalls[r_val] = stalls[max_key]
        if l_val in stalls:
            stalls[l_val] += stalls[max_key]
        else:
            stalls[l_val] = stalls[max_key]

        remain_people -= stalls[max_key]
        del stalls[max_key]

    print(l_val, r_val)

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
