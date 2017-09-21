#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 Code Jam Qualification round
    Problem-B: Tidy Numbers, (simple and slow version)
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

    tc.number = int(sys.stdin.readline())

    return


def is_ascending(number):
    '''
    number: Interger
    return: True if number is ascending order
            False if not ascending order
    '''

    s_number = str(number)

    for idx in range(1, len(s_number)):
        if s_number[idx] < s_number[idx-1]:
            return False

    return True



def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    while not is_ascending(tc.number):
        tc.number -= 1

    print(tc.number)

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
