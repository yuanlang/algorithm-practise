#!/bin/python3
# We define an hourglass in A to be a subset of values with indices falling 
# in this pattern in A's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
# Task
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
# Input Format
# There are 6 lines of input, where each line contains 6 space-separated integers 
# describing 2D Array A
# every value in will be in the inclusive range of -9 to 9.
import math
import os
import random
import re
import sys

# Description:
# calc max hourglass of a matrix
# Note: need to consider the sum < 0


def hourglass_max(arr, row_number, col_number):
    max_sum = -0x7fffffff
    for i in range(0, row_number-2):
        for j in range(0, col_number-2):
            max_sum = max(max_sum, (arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                                    arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]))
    return max_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    # print(arr)
    print(hourglass_max(arr, 6, 6))
