#!/usr/bin/python
# -*- coding: GBK -*-

# 三数之和
# 给你一个包含 n 个整数的数组?nums，判断?nums?中是否存在三个元素 a，b，c ，使得?a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# ?

# 示例：

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvpj16/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List

class Solution:
    # Brute force
    def threeSumV1(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)
        print(sorted_nums)
        length = len(sorted_nums)
        for i in range(length):
            # if duplicate
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            for j in range(i + 1, length):
                if j > i + 1 and sorted_nums[j] == sorted_nums[j - 1]:
                    continue
                for k in range(j + 1, length):
                    if k > j + 1 and sorted_nums[k] == sorted_nums[k - 1]:
                        continue
                    if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0:
                        result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
        return result

    # 根据要求计算数组中满足条件的集合
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        # result = [[-1,2],[0,1]]
        print(nums)
        result = []
        length = len(nums)
        for i in range(length):
            #第二个指针
            j = length - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while i < j and nums[i] + nums[j] > target:
                j -= 1
            if j == i:
                break
            if nums[i] + nums[j] == target:
                result.append([nums[i], nums[j]])
        print(result)
        return result

    def threeSumV2(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)
        print(sorted_nums)
        length = len(sorted_nums)
        for i in range(length):
            # if duplicate
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            two_sum_set = self.twoSum(sorted_nums[i + 1:], 0 - sorted_nums[i])
            for item in two_sum_set:
                result.append([sorted_nums[i]] + item)

        return result

    # V2时间不过，把函数twoSum合入
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # print(nums)
        length = len(nums)
        for i in range(length):
            # if duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            k = length - 1
            for j in range(i+1, length):
                #第二个指针
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    result.append(
                        [nums[i], nums[j], nums[k]])

        return result

if __name__ == "__main__":
    s = Solution()
    l = [-1, 0, 1, 2, -1, -4]
    r = s.threeSum(l)
    print(r)

    l = [0,0,0,0]
    r = s.threeSum(l)
    print(r)
