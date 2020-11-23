#!/usr/bin/python
# -*- coding: GBK -*-

# �ƶ���
# ����һ������ nums����дһ������������ 0 �ƶ��������ĩβ��ͬʱ���ַ���Ԫ�ص����˳��

# ʾ��:

# ����: [0,1,0,3,12]
# ���: [1,3,12,0,0]
# ˵��:

# ������ԭ�����ϲ��������ܿ�����������顣
# �������ٲ���������

# ���ߣ����� (LeetCode)
# ���ӣ�https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2ba4i/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

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
