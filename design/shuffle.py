#!/usr/bin/python
# -*- coding: GBK -*-

# ��������
# ����һ��û���ظ�Ԫ�ص����顣

# ?

# ʾ��:

# // �����ּ��� 1, 2 �� 3 ��ʼ�����顣
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // �������� [1,2,3] �����ؽ�����κ� [1,2,3]�����з��صĸ���Ӧ����ͬ��
# solution.shuffle();

# // �������鵽���ĳ�ʼ״̬[1,2,3]��
# solution.reset();

# // �����������[1,2,3]���Һ�Ľ����
# solution.shuffle();

# ���ߣ����� (LeetCode)
# ���ӣ�https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn6gq1/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

from typing import List
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        # ! ��Ҫʹ��list����ȻԴ��Ŀ��ʹ�õ���ͬһ�ݵ�ַ�ռ�
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
