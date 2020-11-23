#!/usr/bin/python
# -*- coding: GBK -*-

# �ϲ�������������
# ��������������������?nums1 �� nums2�����㽫 nums2 �ϲ���?nums1?�У�ʹ nums1 ��Ϊһ���������顣

# ?

# ˵����

# ��ʼ��?nums1 �� nums2 ��Ԫ�������ֱ�Ϊ?m �� n ��
# ����Լ���?nums1?���㹻�Ŀռ䣨�ռ��С���ڻ����?m + n�������� nums2 �е�Ԫ�ء�
# ?

# ʾ����

# ���룺
# nums1 = [1, 2, 3, 0, 0, 0], m = 3
# nums2 = [2, 5, 6],       n = 3

# �����[1, 2, 2, 3, 5, 6]
# ?

# ��ʾ��

# -10 ^ 9 <= nums1[i], nums2[i] <= 10 ^ 9
# nums1.length == m + n
# nums2.length == n

# Python3


# ���ߣ����� (LeetCode)
# ���ӣ�https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnumcr/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

from typing import List

class Solution:
    def mergev1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #list1��ǰԪ�ش���list2��ǰԪ��ʱ���Ž��н���
        #������Ҫ��֤˳��
        #ѭ��ֱ��ʲô����һ��������û��Ԫ��Ϊֹ
        index1 = 0
        index2 = 0
        remain1 = m
        remain2 = n
        while remain1 > 0 and remain2 > 0:
            # switch
            if nums1[index1] > nums2[index2]:
                nums1[index1], nums2[index2] = nums2[index2], nums1[index1]
                cur_index = index2
                while cur_index + 1 < n and nums2[cur_index] > nums2[cur_index + 1]:
                    nums2[cur_index], nums2[cur_index + 1] = nums2[cur_index + 1], nums2[cur_index]
                    cur_index += 1
            index1 += 1
            remain1 -= 1

        #����ʣ�µ������е�Ԫ��
        while remain2 > 0:
            nums1[index1] = nums2[index2]
            index1 += 1
            index2 += 1
            remain2 -= 1

    # from end to start
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
                
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]

if __name__ == "__main__":
    # expect: True
    # s = Solution()
    # l1 = [1, 2, 3, 0, 0, 0]
    # l2 = [2, 5, 6]
    # s.merge(l1, 3, l2, 3)
    # print(l1)

    # s = Solution()
    # l1 = []
    # l2 = []
    # s.merge(l1, 0, l2, 0)
    # print(l1)

    # s = Solution()
    # l1 = [1]
    # l2 = []
    # s.merge(l1, 1, l2, 0)
    # print(l1)

    # s = Solution()
    # l1 = [0]
    # l2 = [1]
    # s.merge(l1, 0, l2, 1)
    # print(l1)

    # s = Solution()
    # l1 = [1,4,7,0,0,0]
    # l2 = [2,5,8]
    # s.merge(l1, 3, l2, 3)
    # print(l1)

    s = Solution()
    l1 = [4, 5, 6, 0, 0, 0]
    l2 = [1, 2, 3]
    s.merge(l1, 3, l2, 3)
    print(l1)
