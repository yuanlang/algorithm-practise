#!/usr/bin/python
# -*- coding: GBK -*-

# ��һ
# ����һ����������ɵķǿ���������ʾ�ķǸ��������ڸ����Ļ����ϼ�һ��

# ���λ���ִ�����������λ�� ������ÿ��Ԫ��ֻ�洢�������֡�

# ����Լ���������� 0 ֮�⣬��������������㿪ͷ��

# ʾ��?1:

# ����: [1,2,3]
# ���: [1,2,4]
# ����: ���������ʾ���� 123��
# ʾ��?2:

# ����: [4,3,2,1]
# ���: [4,3,2,2]
# ����: ���������ʾ���� 4321��

# ���ߣ����� (LeetCode)
# ���ӣ�https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2cv1c/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

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
