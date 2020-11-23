#!/usr/bin/python
# -*- coding: GBK -*-

# �������Ĳ������
# ����һ�������������㷵���䰴 ������� �õ��Ľڵ�ֵ�� �������أ������ҷ������нڵ㣩��

# ?

# ʾ����
# ��������[3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# �������α��������

# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# ���ߣ����� (LeetCode)
# ���ӣ�https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnldjj/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # ��δ���㼶�����⣬�������ö���Ϊ�յ��ص�
        cur_node = root
        if root == None:
            return []
        result_list = []
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            next_level_queue = deque()
            result_list.append([])
            while len(queue) > 0:
                cur_node = queue.pop()
                if cur_node.left != None:
                    next_level_queue.appendleft(cur_node.left)
                if cur_node.right != None:
                    next_level_queue.appendleft(cur_node.right)
                result_list[-1].append(cur_node.val)
            queue = deque(next_level_queue)

        return result_list
