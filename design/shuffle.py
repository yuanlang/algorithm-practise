#!/usr/bin/python
# -*- coding: GBK -*-

# 打乱数组
# 打乱一个没有重复元素的数组。

# ?

# 示例:

# // 以数字集合 1, 2 和 3 初始化数组。
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
# solution.shuffle();

# // 重设数组到它的初始状态[1,2,3]。
# solution.reset();

# // 随机返回数组[1,2,3]打乱后的结果。
# solution.shuffle();

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn6gq1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        # ! 需要使用list，不然源与目的使用的是同一份地址空间
        self.org = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return list(self.org)

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        new_list = []
        temp_list = list(self.org)
        length = len(temp_list)
        for i in range(length, 0, -1):
            guess = randint(1, i) - 1
            new_list.append(temp_list[guess])
            del(temp_list[guess])
        print(new_list)
        return new_list


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
