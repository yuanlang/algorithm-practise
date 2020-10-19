#!/usr/bin/python
# -*- coding: GBK -*-

# 合并两个有序数组
# 给你两个有序整数数组?nums1 和 nums2，请你将 nums2 合并到?nums1?中，使 nums1 成为一个有序数组。

# ?

# 说明：

# 初始化?nums1 和 nums2 的元素数量分别为?m 和 n 。
# 你可以假设?nums1?有足够的空间（空间大小大于或等于?m + n）来保存 nums2 中的元素。
# ?

# 示例：

# 输入：
# nums1 = [1, 2, 3, 0, 0, 0], m = 3
# nums2 = [2, 5, 6],       n = 3

# 输出：[1, 2, 2, 3, 5, 6]
# ?

# 提示：

# -10 ^ 9 <= nums1[i], nums2[i] <= 10 ^ 9
# nums1.length == m + n
# nums2.length == n

# Python3


# 作者：力扣 (LeetCode)
# 链接：https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnumcr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List

class Solution:
    def mergev1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #list1当前元素大于list2当前元素时，才进行交换
        #交换需要保证顺序
        #循环直到什么问题一个数组中没有元素为止
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

        #处理剩下的数组中的元素
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
