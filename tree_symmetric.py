#!/usr/bin/python
# -*- coding: GBK -*-

# �Գƶ�����
# ����һ����������������Ƿ��Ǿ���ԳƵġ�

# ?

# ���磬������?[1, 2, 2, 3, 4, 4, 3] �ǶԳƵġ�

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# ?

# �����������?[1,2,2,null,3,null,3] ���Ǿ���ԳƵ�:

#     1
#    / \
#   2   2
#    \   \
#    3    3
# ?

# ���ף�

# ��������õݹ�͵������ַ���������������

# ���ߣ����� (LeetCode)
# ���ӣ�https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn7ihv/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #  ����һ�����У��������Ƚ�
    def isSymmetricQueue(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.checkIterative(root, root)

    def checkIterative(self, p, q) -> bool:
        queue = deque()
        queue.appendleft(p)
        queue.appendleft(q)
        while len(queue) > 0:
            left = queue.pop()
            right = queue.pop()
            #������Ϊ�շ���true
            if left == None and right == None:
                continue
            #ֻ������һ��Ϊ�գ�����False
            if left == None or right == None or left.val != right.val:
                return False
            queue.appendleft(left.left)
            queue.appendleft(right.right)
            queue.appendleft(left.right)
            queue.appendleft(right.left)
            print(queue)


    #  ���õݹ鷽ʽ��ʵ��
    def isSymmetricRecursive(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.check(root, root)

    def checkRecursive(self, left, right) -> bool:
        #������Ϊ�շ���true
        if left == None and right == None:
            return True
        #ֻ������һ��Ϊ�գ�����False
        if left == None or right == None:
            return False
        #����Ϊ��ձȽϵ�ǰֵ�Լ�������ֵ
        return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)

    #���ò�α�����ÿһ��Ľ��Ӧ�ö��ǿ����
    def isSymmetricLayer(self, root: TreeNode) -> bool:
        if root == None:
            return True
        val_list = []
        self.inLayerOrder(root, val_list)
        print(val_list)
        cur_start = 0
        cur_end = 1
        cur_round = 1
        length = len(val_list)
        while cur_end <= length:
            temp = val_list[cur_start:cur_end]
            print("temp: ", temp)
            if temp != temp[-1::-1]:
                return False
            #�Ѿ��������ڵ������ֱ�ӷ���True
            if cur_end == length:
                return True
            cur_round += 1
            cur_start = cur_end
            cur_end = 2 ** cur_round - 1
            if cur_end > length:
                return False

        return True

    def inLayerOrder(self, root: TreeNode, val_list: List):
        queue = [root]
        while len(queue) > 0:
            node = queue.pop()
            if node == None:
                val_list.append(None)
                continue
            val_list.append(node.val)
            if node.left:
                queue.insert(0, node.left)
            elif node.right:
                queue.insert(0, None)

            if node.right:
                queue.insert(0, node.right)
            elif node.left:
                queue.insert(0, None)

        #���ǲ�������Ԫ��ΪNone
        length = len(val_list)
        end = 2 ** (int(math.log2(length))+1) - 1
        for i in range(length, end):
            val_list.append(None)

    #��������������Աȷ�ת���Ƿ���ԭ������ͬ���ж�
    def isSymmetricV1(self, root: TreeNode) -> bool:
        if root == None:
            return True

        val_list = []
        self.inorder(root, val_list)
        print(val_list)
        return val_list == val_list[-1::-1]

    def inorder(self, root: TreeNode, val_list: List) -> None:
        if root.left:
            self.inorder(root.left, val_list)
        elif root.right:
            val_list.append(None)

        val_list.append(root.val)
        if root.right:
            self.inorder(root.right, val_list)
        elif root.left:
            val_list.append(None)
