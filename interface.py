class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        arr = [n]
        # print("I implemented: AdvancedArithmetic")
        for i in range(1, int(n/2)+1):
            if n % i == 0:
                arr.append(i)
        # print(arr)
        return sum(arr)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
