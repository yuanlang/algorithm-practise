#!/usr/bin/python
# -*- coding: GBK -*-

# 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 示例:

# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:

# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2ba4i/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List

class Solution:
    def moveZeroesOld(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                for j in range(i, n-1):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                # print(nums)
                n -= 1
            else:
                i += 1

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        new_index = 0
        for i in range(n):
            if nums[i] != 0:
                nums[new_index] = nums[i]
                new_index += 1
                # print(nums)
        for i in range(new_index, n):
            nums[i] = 0


if __name__ == "__main__":
    s = Solution()
    l = [0, 1, 2, 3, 0]
    s.moveZeroes(l)
    print(l)
    l = [0, 0, 2, 3, 12]
    s.moveZeroes(l)
    print(l)
