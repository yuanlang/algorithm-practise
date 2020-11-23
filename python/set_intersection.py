#!/usr/bin/python
# -*- coding: GBK -*-

# ��������Ľ��� II
# �����������飬��дһ���������������ǵĽ�����

# ?

# ʾ�� 1��

# ���룺nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# �����[2, 2]
# ʾ�� 2:

# ���룺nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# �����[4, 9]
# ?

# ˵����

# ��������ÿ��Ԫ�س��ֵĴ�����Ӧ��Ԫ�������������г��ִ�������Сֵһ�¡�
# ���ǿ��Բ�������������˳��
# ���ף�

# ��������������Ѿ��ź����أ��㽫����Ż�����㷨��
# ���?nums1?�Ĵ�С��?nums2?С�ܶ࣬���ַ������ţ�
# ���?nums2?��Ԫ�ش洢�ڴ����ϣ��ڴ������޵ģ������㲻��һ�μ������е�Ԫ�ص��ڴ��У������ô�죿

# ���ߣ�����(LeetCode)
# ���ӣ�https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2y0c2/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

from typing import List

class Solution:
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result_list = []
        len_1 = len(nums1)
        len_2 = len(nums2)

        nums1.sort()
        nums2.sort()
        index_1 = 0
        index_2 = 0
        while index_1 < len_1 and index_2 < len_2:
            if nums1[index_1] == nums2[index_2]:
                result_list.append(nums2[index_2])
                index_1 += 1
                index_2 += 1
            elif nums1[index_1] > nums2[index_2]:
                index_2 += 1
            else:
                index_1 += 1

        return result_list

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result_list = []
        set_list_1 = set(nums1)
        set_list_2 = set(nums2)

        intersection = set_list_1.intersection(set_list_2)
        for item in intersection:
            result_list += [item for i in range(
                min(nums1.count(item), nums2.count(item)))]

        return result_list


if __name__ == "__main__":
    s = Solution()
    print(s.intersect1([1, 2, 2, 1], [2, 2]))
    print(s.intersect([1, 2, 2, 1], [2, 2]))

    print(s.intersect1([4, 9, 5], [9, 4, 9, 8, 4]))
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))

    print(s.intersect1([1, 2, 2, 1], [2]))
    print(s.intersect([1, 2, 2, 1], [2]))
