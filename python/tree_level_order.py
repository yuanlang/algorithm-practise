#!/usr/bin/python
# -*- coding: GBK -*-

# 二叉树的层序遍历
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

# ?

# 示例：
# 二叉树：[3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：

# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnldjj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

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
        # 如何处理层级的问题，可以利用队列为空的特点
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
