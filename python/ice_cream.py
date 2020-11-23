#!/bin/python3
# Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money 
# to buy ice cream. On any given day, the parlor offers a line of flavors. 
# Each flavor has a cost associated with it.
# Given the value of money and the cost of each flavor for t trips to the Ice Cream Parlor,
#  help Sunny and Johnny choose two distinct flavors such that they spend their entire 
# pool of money during each visit. ID numbers are the 1 - based index number associated 
# with a . For each trip to the parlor, print the ID numbers for the two types of ice 
# cream that Sunny and Johnny purchase as two space-separated integers on a new line. 
# You must print the smaller ID first and the larger ID second.
# For example, there are n=5 flavors having cost=[2,1,3,5,6]. 
# Together they have money = 5 to spend. 
# They would purchase flavor ID's 1 and 3 for a cost of 2 + 3 = 5. 
# Use 1 based indexing for your response.
# Note:
# Two ice creams having unique IDs i and j may have the same cost(i.e., cost[i] = cost[j]).
# There will always be a unique solution.
import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.


def whatFlavors(cost, money):
    i = 1
    m = {}
    for c in cost:
        if c not in m:
            m[c] = []
        m[c].append(i)
        i += 1
    # print(m)

    for c in m.keys():
        first = m[c][0]
        second = 0
        remain = money - c
        if remain in m.keys():
            if remain != c:
                second = m[remain][0]
            elif len(m[remain]) == 1:
                continue
            else:
                second = m[remain][1]
            print(first, second)
            break


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
