# Objective
# Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the Tutorial tab for a video on testing!
# Task
# Your local library needs your help! Given the expected and actual return dates 
# for a library book, create a program that calculates the fine(if any). 
# The fee structure is as follows:
# If the book is returned on or before the expected return date, 
# no fine will be charged(i.e.: fine=0.
# If the book is returned after the expected return day but still 
# within the same calendar month and year as the expected return date, 
# fine = 15 Hackos x (the number of dalay days).
# If the book is returned after the expected return month but still within 
# the same calendar year as the expected return date, 
# the fine = 500 Hackos x (the number of dalay months).
# If the book is returned after the calendar year in which it was expected, 
# there is a fixed fine of 10000.

def charge(Actual, Expected):
    ActualDay = int(Actual[0])
    ActualMonth = int(Actual[1])
    ActualYear = int(Actual[2])
    ExpectedDay = int(Expected[0])
    ExpectedMonth = int(Expected[1])
    ExpectedYear = int(Expected[2])

    fine = 0
    # small or euqal, no fine
    if ActualYear < ExpectedYear:
        return 0
    elif ActualYear == ExpectedYear:
        #same month
        if ActualMonth < ExpectedMonth:
            return 0
        elif ActualMonth == ExpectedMonth:
            if ActualDay <= ExpectedDay:
                fine = 0
                return fine
            else:
                fine = 15 * (ActualDay - ExpectedDay)
                return fine
        #diff month
        else:
            fine = 500 * (ActualMonth - ExpectedMonth)
            return fine

    #diff year
    else:
        fine = 10000
        return fine

# Actual
s1 = input().split()

# Expected
s2 = input().split()

# print(s1)
# print(s2)

print(charge(s1, s2))
