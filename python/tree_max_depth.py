#!/usr/bin/python
# -*- coding: GBK -*-

# ��������������
# ����һ�����������ҳ��������ȡ�

# �����������Ϊ���ڵ㵽��ԶҶ�ӽڵ���·���ϵĽڵ�����

# ˵��: Ҷ�ӽڵ���ָû���ӽڵ�Ľڵ㡣

# ʾ����
# ����������[3, 9, 20, null, null, 15, 7]��

#     3
#    / \
#   9  20
#     /  \
#    15   7
# ��������������?3 ��

# ���ߣ����� (LeetCode)
# ���ӣ�https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnd69e/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # �ǵݹ�ⷨ
    def maxDepthNoRecursive(self, root: TreeNode) -> int:
        if root == None:
            return 0
        max_depth = 0
        node_queue = []
        depth_queue = []
        cur_node = root
        cur_depth = 1
        node_queue.append(cur_node)
        depth_queue.append(cur_depth)
        while len(node_queue) != 0:
            # ���ʵ�ǰ�ڵ�
            max_depth = max(cur_depth, max_depth)
            if cur_node.left != None:
                node_queue.append(cur_node.left)
                depth_queue.append(cur_depth + 1)
            if cur_node.right != None:
                node_queue.append(cur_node.right)
                depth_queue.append(cur_depth + 1)
            #ÿ��ȡ����β
            cur_node = node_queue[0]
            del(node_queue[0])
            cur_depth = depth_queue[0]
            del(depth_queue[0])

        return max_depth

    # �ݹ�ⷨ
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        max_depth = 0
        #���ΪҶ�ӽڵ㣬�򷵻����Ϊ1
        if root.left == None and root.right == None:
            return 1
        if root.left != None:
            max_depth = max(max_depth, 1 + self.maxDepth(root.left))
        if root.right != None:
            max_depth = max(max_depth, 1 + self.maxDepth(root.right))

        return max_depth
