#!/usr/bin/python
# -*- coding: GBK -*-

# 旋转图像
# 给定一个 n?×?n 的二维矩阵表示一个图像。

# 将图像顺时针旋转 90 度。

# 说明：

# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

# 示例 1:

# 给定 matrix =
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ],

# 原地旋转输入矩阵，使其变为:
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]
# 示例 2:

# 给定 matrix =
# [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ],

# 原地旋转输入矩阵，使其变为:
# [
#     [15, 13, 2, 5],
#     [14, 3, 4, 1],
#     [12, 6, 8, 9],
#     [16, 7, 10, 11]
# ]

# 作者：力扣(LeetCode)
# 链接：https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnhhkv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n < 2:
            return

        #先调转各行
        for i in range(int(n/2)):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

        #沿对称线反转元素
        for i in range(n):
            for j in range(n):
                # 对称线不用交换
                if i == j:
                    continue
                #只交换上三角
                if i > j:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    # expect: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    s = Solution()
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(l)
    print(l)
    # expect: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    l = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(l)
    print(l)
