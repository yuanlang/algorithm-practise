#!/usr/bin/python
# -*- coding: GBK -*-

# 最大子序和
# 给定一个整数数组 nums?，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 输出: 6
# 解释: 连续子数组?[4, -1, 2, 1] 的和最大，为?6。
# 进阶:

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


# Python3


# 作者：力扣(LeetCode)
# 链接：https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn3cg3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List

class Solution:
    def maxSubArrayv1(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        #从最后一个数向前组合，并求出最大值
        max_value = -float('inf')
        for i in range(length):
            max_value = max(sum(nums[length-1-i:length]), max_value)

        max_value = max(max_value, self.maxSubArray(nums[:-1]))
        return max_value

    def maxSubArrayv2(self, nums: List[int]) -> int:
        #用一个数组存储所有组合的最大值
        length = len(nums)
        max_value_array = [-float('inf') for i in range(length+1)]
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        for i in range(length):
            temp = nums[:i+1]
            temp_len = len(temp)
            # 更新长度为1的最大值
            if temp_len == 1:
                max_value_array[1] = max(max_value_array[1], temp[0])
            for j in range(temp_len):
                max_value_array[j+1] = max(max_value_array[j+1],
                                           sum(temp[temp_len-j-1:]))
        # 返回所有大小的最大值
        return max(max_value_array)

    #动态规划
    def maxSubArraydp(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        #用一个数组存储所有组合的最大值
        max_value_list = [0 for i in range(length)]
        max_value_list[0] = nums[0]
        for i in range(1, length):
            max_value_list[i] = max(max_value_list[i-1] + nums[i], nums[i])
        return max(max_value_list)

    #贪心法
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, length):
            if cur_sum > 0:
                cur_sum = cur_sum + nums[i]
            else:
                cur_sum = nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum

if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4, 3]) == 8
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4, 3, -5]) == 8
