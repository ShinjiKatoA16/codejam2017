#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 Code Jam Qualification round
    Problem-B: Tidy Numbers
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

    x = list(sys.stdin.readline())
    tc.num_list = [int(i) for i in x if i != '\n']

    return


def set99(num_list, pos):
    while pos < len(num_list):
        num_list[pos] = 9
        pos += 1

    return


def check_list(num_list):
    for idx in range(len(num_list) - 1):
        if num_list[idx] > num_list[idx+1]:
            if num_list[idx] == 0:
                num_list[idx] = 9
            else:
                num_list[idx] -= 1
            set99(num_list, idx+1)
            check_list(num_list)

    return


def numlist2str(numlist):
    ret_str = ''
    if numlist[0] != 0:
        ret_str += str(numlist[0])

    for i in range(1, len(numlist)):
        ret_str += str(numlist[i])

    return ret_str


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    check_list(tc.num_list)

    print(numlist2str(tc.num_list))

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
