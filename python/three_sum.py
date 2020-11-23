#!/usr/bin/python
# -*- coding: GBK -*-

# ����֮��
# ����һ������ n ������������?nums���ж�?nums?���Ƿ��������Ԫ�� a��b��c ��ʹ��?a + b + c = 0 �������ҳ��������������Ҳ��ظ�����Ԫ�顣

# ע�⣺���в����԰����ظ�����Ԫ�顣

# ?

# ʾ����

# �������� nums = [-1, 0, 1, 2, -1, -4]��

# ����Ҫ�����Ԫ�鼯��Ϊ��
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# ���ߣ����� (LeetCode)
# ���ӣ�https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvpj16/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

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

    # ����Ҫ��������������������ļ���
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        # result = [[-1,2],[0,1]]
        print(nums)
        result = []
        length = len(nums)
        for i in range(length):
            #�ڶ���ָ��
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

    # V2ʱ�䲻�����Ѻ���twoSum����
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
                #�ڶ���ָ��
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
