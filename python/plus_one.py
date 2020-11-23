#!/usr/bin/python
# -*- coding: GBK -*-

# 加一
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例?1:

# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例?2:

# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2cv1c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result_list = []
        n = len(digits)
        if n == 0:
            return [1]
        add_one = 1
        for i in range(n, 0, -1):
            if digits[i-1] + add_one == 10:
                result_list.insert(0, 0)
                add_one = 1
            else:
                result_list.insert(0, digits[i-1] + add_one)
                add_one = 0
        if add_one == 1:
            result_list.insert(0, add_one)
        return result_list


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([4, 3, 2, 1]))
    print(s.plusOne([1, 9, 9]))
    print(s.plusOne([9]))
