# Objective
# Today we're learning about running time! Check out the Tutorial tab for 
# learning materials and an instructional video!
# Task
# A prime is a natural number greater than 1 that has no positive divisors 
# other than 1 and itself. Given a number, n, determine and print whether 
# it's Prime or Not Prime.
import math
count = int(input())
for i in range(count):
    number = int(input())
    result = True

    if number == 1:
        print("Not prime")
        continue

    for j in range(2, int(math.sqrt(number))+1):
        if number % j == 0:
            result = False

    if result:
        print("Prime")
    else:
        print("Not prime")
