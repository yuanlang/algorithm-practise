# Enter your code here. Read input from STDIN. Print output to STDOUT
# Task
# Given  names and phone numbers, assemble a phone book that maps 
# friends' names to their respective phone numbers. 
# You will then be given an unknown number of names to query your phone book for. 
# For each  queried, print the associated entry from your phone book 
# on a new line in the form name = phoneNumber
# if an entry for is not found, print Not found instead.
# Note: Your phone book should be a Dictionary / Map / HashMap data structure.

n = (int)(input())
m = {}
for i in range(n):
    s = input()
    name, phone = s.split(" ")
    m[name] = phone

while True:
    try:
        q = input()
        if q in m:
            print(q + "=" + m[q])
        else:
            print("Not found")
    except EOFError:
        # print ("EOFError")
        break
