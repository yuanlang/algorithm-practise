#!/usr/bin/python
# -*- coding: GBK -*-

# 两个数组的交集 II
# 给定两个数组，编写一个函数来计算它们的交集。

# ?

# 示例 1：

# 输入：nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# 输出：[2, 2]
# 示例 2:

# 输入：nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# 输出：[4, 9]
# ?

# 说明：

# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。
# 进阶：

# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果?nums1?的大小比?nums2?小很多，哪种方法更优？
# 如果?nums2?的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

# 作者：力扣(LeetCode)
# 链接：https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2y0c2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

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
