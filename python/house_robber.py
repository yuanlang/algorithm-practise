#!/usr/bin/python
# -*- coding: GBK -*-

# 198. ��ҽ���
# ����һ��רҵ��С͵���ƻ�͵���ؽֵķ��ݡ�ÿ�䷿�ڶ�����һ�����ֽ�Ӱ����͵�Ե�Ψһ��Լ���ؾ������ڵķ���װ���໥��ͨ�ķ���ϵͳ������������ڵķ�����ͬһ���ϱ�С͵���룬ϵͳ���Զ�������

# ����һ������ÿ�����ݴ�Ž��ķǸ��������飬������ ����������װ�õ������ ��һҹ֮���ܹ�͵�Ե�����߽�


# ʾ�� 1��

# ���룺[1, 2, 3, 1]
# �����4
# ���ͣ�͵�� 1 �ŷ���(���=1) ��Ȼ��͵�� 3 �ŷ���(���=3)��
# ͵�Ե�����߽�� = 1 + 3 = 4 ��
# ʾ�� 2��

# ���룺[2, 7, 9, 3, 1]
# �����12
# ���ͣ�͵�� 1 �ŷ���(���=2), ͵�� 3 �ŷ���(���=9)������͵�� 5 �ŷ���(���=1)��
# ͵�Ե�����߽�� = 2 + 9 + 1 = 12 ��


# ��ʾ��

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        dp = [nums[0], max(nums[:2])]
        for i in range(2, n):
            dp.append(max(nums[i] + dp[i-2], dp[i-1]))
        print(dp)
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.rob([1,2,3,1]))
    print(s.rob([2, 7, 9, 3, 1]))