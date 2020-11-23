#Write your code here
# Sample Input
# 4
# 3 5
# 2 4
# -1 - 2
# -1 3

# Sample Output
# 243
# 16
# n and p should be non-negative
# n and p should be non-negative

class Calculator:
    def __init__(self):
        return

    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        if p == 0:
            return 1
        result = n
        for i in range(2, p+1):
            result *= n
        return result


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
