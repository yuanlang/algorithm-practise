#!/bin/python3
# Task:
# Given a base-10 integer, , convert it to binary(base-2). 
# Then find and print the base-10 integer denoting the maximum number 
# of consecutive 1's in n's binary representation.
# Input Format:
# A single integer, n.
# Sample Input 1
# 5
# Sample Output 1
# 1
# Sample Input 2
# 13
# Sample Output 2
# 2
# Explanation
# Sample Case 1:
# The binary representation of 5 is 101 , so the maximum number of consecutive 1's is 1.
# Sample Case 2:
# The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.

import math
import os
import random
import re
import sys

def max_conse_old(n):
    if n == 0:
        return 0
    bin_n = bin(n)
    max_occour = 0
    cur_occour = 0
    start = False
    for i in bin_n[2:]:
        # start to count
        if i == '1' and start == False:
            start = True
            cur_occour += 1
        elif start == True:
            # end to compare
            if i == '0':
                start = False
                # reset the cur_occour
                cur_occour = 0
                # print("max_occour", max_occour)
            else:
                cur_occour += 1
        max_occour = max(max_occour, cur_occour)
    return max_occour


def max_conse(n):
    max_occour = 0
    cur_occour = 0
    start = False
    while n > 0:
        remain = n % 2
        n = int(n / 2)
        # start to count
        if remain == 1 and start == False:
            start = True
            cur_occour += 1
        elif start == True:
            # end to compare
            if remain == 0:
                start = False
                # reset the cur_occour
                cur_occour = 0
                print("max_occour", max_occour)
            else:
                cur_occour += 1
        max_occour = max(max_occour, cur_occour)
    return max_occour

if __name__ == '__main__':
    n = int(input())
    print(bin(n))
    print(max_conse(n))
