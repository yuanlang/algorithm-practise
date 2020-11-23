#!/usr/bin/python
# -*- coding: GBK -*-

# ��תͼ��
# ����һ�� n?��?n �Ķ�ά�����ʾһ��ͼ��

# ��ͼ��˳ʱ����ת 90 �ȡ�

# ˵����

# �������ԭ����תͼ������ζ������Ҫֱ���޸�����Ķ�ά�����벻Ҫʹ����һ����������תͼ��

# ʾ�� 1:

# ���� matrix =
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ],

# ԭ����ת�������ʹ���Ϊ:
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]
# ʾ�� 2:

# ���� matrix =
# [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ],

# ԭ����ת�������ʹ���Ϊ:
# [
#     [15, 13, 2, 5],
#     [14, 3, 4, 1],
#     [12, 6, 8, 9],
#     [16, 7, 10, 11]
# ]

# ���ߣ�����(LeetCode)
# ���ӣ�https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnhhkv/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n < 2:
            return

        #�ȵ�ת����
        for i in range(int(n/2)):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

        #�ضԳ��߷�תԪ��
        for i in range(n):
            for j in range(n):
                # �Գ��߲��ý���
                if i == j:
                    continue
                #ֻ����������
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
