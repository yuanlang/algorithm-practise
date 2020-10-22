#!/usr/bin/python
# -*- coding: GBK -*-

# ��֤����������
# ����һ�����������ж����Ƿ���һ����Ч�Ķ�����������

# ����һ��������������������������

# �ڵ��������ֻ����С�ڵ�ǰ�ڵ������
# �ڵ��������ֻ�������ڵ�ǰ�ڵ������
# �������������������������Ҳ�Ƕ�����������
# ʾ��?1:

# ����:
#     2
#    / \
#   1   3
# ���: true
# ʾ��?2:

# ����:
#     5
#    / \
#   1   4
# ?    / \
# ?   3   6
# ���: false
# ����: ����Ϊ: [5,1,4,null,null,3,6]��
# ?    ���ڵ��ֵΪ 5 �����������ӽڵ�ֵΪ 4 ��

# ���ߣ����� (LeetCode)
# ���ӣ�https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn08xg/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #����ⷨ�����⣬û�п�������ĸ��ڵ�Ƚ�
    def isValidBSTv1(self, root: TreeNode) -> bool:
        result = True
        if root == None:
            return True
        if root.left != None and root.left.val >= root.val:
            return False
        if root.right != None and root.right.val <= root.val:
            return False
        result = result and self.isValidBST(
            root.left) and self.isValidBST(root.right)
        return result

    #�����������������Ĺ������Υ���ǲ�����
    def isValidBST(self, root: TreeNode) -> bool:
        result = True
        #��������󣬴�������
        mid_list = []
        #�������ӽڵ�
        stack = []
        cur_node = root
        pre_val = float('-inf')  # ����-0x7fffffff��������
        while len(stack) > 0 or cur_node:
            #һֱ�ߵ�������������ڵ�
            while cur_node != None:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            mid_list.append(cur_node.val)
            if cur_node.val <= pre_val:
                return False
            #��¼���һ�εĽڵ�ֵ
            pre_val = cur_node.val
            #������ҽڵ�������ҽڵ㣬��ʹΪ��
            cur_node = cur_node.right

        print(mid_list)

        #�ж������Ƿ�����

        return result
