#!/bin/python3

# Given an array, a, of size n distinct elements, sort the array in ascending 
# order using the Bubble Sort algorithm above. Once sorted, print the following 3 lines:
# 1. Array is sorted in numSwaps swaps.
# where numSwaps is the number of swaps that took place.
# 2. First Element: firstElement
# where firstElement is the first element in the sorted array.
# 3. Last Element: lastElement
# where is the last element in the sorted array.
# Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numberOfSwaps = 0
for i in range(n-1):
    numberOfSwapsThisTurn = 0
    for j in range(i+1, n):
        if (a[i] > a[j]):
            a[j], a[i] = a[i], a[j]
            numberOfSwapsThisTurn += 1
    if numberOfSwapsThisTurn == 0:
        break
    numberOfSwaps += numberOfSwapsThisTurn

print("Array is sorted in " + str(numberOfSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
