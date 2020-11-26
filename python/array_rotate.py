#!/usr/bin/python
# -*- coding: GBK -*-

# ��ת����
# ����һ�����飬�������е�Ԫ�������ƶ�?k?��λ�ã�����?k?�ǷǸ�����

# ʾ�� 1:

# ����: [1, 2, 3, 4, 5, 6, 7] �� k = 3
# ���: [5, 6, 7, 1, 2, 3, 4]
# ����:
# ������ת 1 ��: [7, 1, 2, 3, 4, 5, 6]
# ������ת 2 ��: [6, 7, 1, 2, 3, 4, 5]
# ������ת 3 ��: [5, 6, 7, 1, 2, 3, 4]
# ʾ��?2:

# ����: [-1, -100, 3, 99] �� k = 2
# ���: [3, 99, -1, -100]
# ����:
# ������ת 1 ��: [99, -1, -100, 3]
# ������ת 2 ��: [3, 99, -1, -100]
# ˵��:

# �������������Ľ�����������������ֲ�ͬ�ķ������Խ��������⡣
# Ҫ��ʹ�ÿռ临�Ӷ�Ϊ?O(1) ��?ԭ��?�㷨��

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        for _i in range(k):
            #ÿ��ֻ�ƶ�һ������
            #tempʼ��ָ�����һ������
            temp = nums[n-1]
            #�Ӻ���ǰ����
            for j in range(n-1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = temp
            # print(nums)

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    s.rotate(nums, 3)
    print(nums)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [1,2,3,4,5,6,7]
    s.rotate(nums, 4)
    print(nums)
    assert nums == [4, 5, 6, 7, 1, 2, 3]

    nums = []
    s.rotate(nums, 3)
    print(nums, nums == [], len(nums))
    assert len(nums) == 0
