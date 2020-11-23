#!/usr/bin/python
# -*- coding: GBK -*-

# ��������
# ����һ���������� nums?���ҵ�һ���������͵����������飨���������ٰ���һ��Ԫ�أ������������͡�

# ʾ��:

# ����: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# ���: 6
# ����: ����������?[4, -1, 2, 1] �ĺ����Ϊ?6��
# ����:

# ������Ѿ�ʵ�ָ��Ӷ�Ϊ O(n) �Ľⷨ������ʹ�ø�Ϊ����ķ��η���⡣


# Python3


# ���ߣ�����(LeetCode)
# ���ӣ�https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn3cg3/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

from typing import List

class Solution:
    def maxSubArrayv1(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        #�����һ������ǰ��ϣ���������ֵ
        max_value = -float('inf')
        for i in range(length):
            max_value = max(sum(nums[length-1-i:length]), max_value)

        max_value = max(max_value, self.maxSubArray(nums[:-1]))
        return max_value

    def maxSubArrayv2(self, nums: List[int]) -> int:
        #��һ������洢������ϵ����ֵ
        length = len(nums)
        max_value_array = [-float('inf') for i in range(length+1)]
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        for i in range(length):
            temp = nums[:i+1]
            temp_len = len(temp)
            # ���³���Ϊ1�����ֵ
            if temp_len == 1:
                max_value_array[1] = max(max_value_array[1], temp[0])
            for j in range(temp_len):
                max_value_array[j+1] = max(max_value_array[j+1],
                                           sum(temp[temp_len-j-1:]))
        # �������д�С�����ֵ
        return max(max_value_array)

    #��̬�滮
    def maxSubArraydp(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        #��һ������洢������ϵ����ֵ
        max_value_list = [0 for i in range(length)]
        max_value_list[0] = nums[0]
        for i in range(1, length):
            max_value_list[i] = max(max_value_list[i-1] + nums[i], nums[i])
        return max(max_value_list)

    #̰�ķ�
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
