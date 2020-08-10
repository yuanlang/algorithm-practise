#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.


def maxSubsetSum_old(arr):
    print(arr)
    length = len(arr)
    # if length == 0:
    #     return 0;
    if length <= 2:
        return arr[0]
    if length == 3:
        return max(arr[0], arr[0]+arr[2])
    q = -0x7fffffff
    for i in range(length):
        for s in range(2, length-i):
            q = max(q, arr[i] + maxSubsetSum(arr[i+s:]))
            print(i, s, q, arr)
    return q

#time out
def maxSubsetSum_list(arr):
    length = len(arr)
    result = []
    # result = [-0x7fffffff] * length
    # for i in range(length):
    #     result.append()
    result.append(arr[0])
    result.append(arr[1])
    for i in range(2, length):
        q = -0x7fffffff
        for j in range(2, i+1):
            q = max(q, arr[i] + result[i-j])
        result.append(q)
    # print(result)
    return max(result)

#List to dict version. still timeout
def maxSubsetSum_dict(arr):
    length = len(arr)
    result = {}
    # convert list to dict
    dict_arr = {k: v for k, v in enumerate(arr)}
    result[0] = dict_arr[0]
    result[1] = dict_arr[1]
    for i in range(2, length):
        q = dict_arr[i]
        for j in range(2, i+1):
            q = max(q, dict_arr[i] + result[i-j])
        result[i] = q

    # print(result)
    return max(result.values())

#Final version
#note:
# 1. store the max value of all previous position instead of current postion
# 2. compute the max from tail to head, instead of from head to tail
def maxSubsetSum(arr):
    length = len(arr)
    result = {}
    result[0] = arr[0]
    result[1] = max(arr[0], arr[1])
    for i, num in enumerate(arr[2:], start=2):
        result[i] = max(result[i-1], result[i-2]+num, result[i-2], num)

    # print(result)
    return result[length-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
