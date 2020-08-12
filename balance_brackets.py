#!/bin/python3

# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
# Two brackets are considered to be a matched pair if the an opening bracket 
# (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) 
# of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().
# A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. 
# For example, {[(])} is not balanced because the contents in between { and } are not balanced. 
# The pair of square brackets encloses a single, unbalanced opening bracket, (, 
# and the pair of parentheses encloses a single, unbalanced closing square bracket, ].
# By this logic, we say a sequence of brackets is balanced if the following conditions are met:
# It contains no unmatched brackets.
# The subset of brackets enclosed within the confines of a matched pair of brackets is also 
# a matched pair of brackets.
# Given  strings of brackets, determine whether each sequence of brackets is balanced. 
# If a string is balanced, return YES. Otherwise, return NO.

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.


def isBalanced(s):
    p = {']': '[', '}': '{', ')': '('}
    result = "YES"
    t = []
    # print(s)
    for c in s:
        if c == '[' or c == '{' or c == '(':
            t.append(c)
        elif len(t) > 0 and t[-1] == p[c]:
            t.pop()
        else:
            return "NO"
        print(c, t)

    if len(t) != 0:
        result = "NO"
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
