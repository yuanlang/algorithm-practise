#!/usr/bin/python
# -*- coding: GBK -*-

# 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。

# ?

# 例如，二叉树?[1, 2, 2, 3, 4, 4, 3] 是对称的。

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# ?

# 但是下面这个?[1,2,2,null,3,null,3] 则不是镜像对称的:

#     1
#    / \
#   2   2
#    \   \
#    3    3
# ?

# 进阶：

# 你可以运用递归和迭代两种方法解决这个问题吗？

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn7ihv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #  利用一个队列，并两两比较
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
            #两个都为空返回true
            if left == None and right == None:
                continue
            #只有其中一个为空，返回False
            if left == None or right == None or left.val != right.val:
                return False
            queue.appendleft(left.left)
            queue.appendleft(right.right)
            queue.appendleft(left.right)
            queue.appendleft(right.left)
            print(queue)


    #  利用递归方式的实现
    def isSymmetricRecursive(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.check(root, root)

    def checkRecursive(self, left, right) -> bool:
        #两个都为空返回true
        if left == None and right == None:
            return True
        #只有其中一个为空，返回False
        if left == None or right == None:
            return False
        #都不为则空比较当前值以及子树的值
        return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)

    #利用层次遍历，每一层的结果应该都是可逆的
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
            #已经遍历完在的情况下直接返回True
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

        #考虑补齐空余的元素为None
        length = len(val_list)
        end = 2 ** (int(math.log2(length))+1) - 1
        for i in range(length, end):
            val_list.append(None)

    #利用中序遍历，对比反转后是否与原中序相同来判断
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
