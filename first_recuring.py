#!/usr/bin/python
# -*- coding: GBK -*-

#Google Question
#Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]:
#It should return 2

#Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]:
#It should return 1

#Given an array = [2, 3, 4, 5]:
#It should return undefined

# Bonus... What if we had this:
# [2, 5, 5, 2, 3, 5, 1, 2, 4]
# return 5 because the pairs are before 2, 2


def firstRecurringCharacterv1(input):
    length = len(input)
    min_occour = float('inf')
    for i in range(length):
        for j in range(i + 1, length):
            if input[j] == input[i] and min_occour > j:
                min_occour = j
    if min_occour > length:
        return None
    else:
        return input[min_occour]

# 利用dict实现，如果dict中存在，则返回当前值
def firstRecurringCharacter(input):
    temp_dict = {}
    length = len(input)
    for i in range(length):
        if input[i] not in temp_dict:
            temp_dict[input[i]] = True
        else:
            return input[i]
    return None

if __name__ == "__main__":
    input = [2, 5, 1, 2, 3, 5, 1, 2, 4]
    ret = firstRecurringCharacter(input)
    print('ret = ', ret)
    assert ret == 2

    input = [2, 1, 1, 2, 3, 5, 1, 2, 4]
    ret = firstRecurringCharacter(input)
    print('ret = ', ret)
    assert ret == 1

    input = [2, 3, 4, 5]
    ret = firstRecurringCharacter(input)
    print('ret = ', ret)
    assert ret == None

    input = [2, 5, 5, 2, 3, 5, 1, 2, 4]
    ret = firstRecurringCharacter(input)
    print('ret = ', ret)
    assert ret == 5
