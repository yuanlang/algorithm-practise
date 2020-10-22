#!/usr/bin/python
# -*- coding: GBK -*-

# 验证二叉搜索树
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 假设一个二叉搜索树具有如下特征：

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例?1:

# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例?2:

# 输入:
#     5
#    / \
#   1   4
# ?    / \
# ?   3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# ?    根节点的值为 5 ，但是其右子节点值为 4 。

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn08xg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #这个解法有问题，没有考虑与根的父节点比较
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

    #利用中序遍历后有序的规则，如果违反是不符合
    def isValidBST(self, root: TreeNode) -> bool:
        result = True
        #中序遍历后，存入数组
        mid_list = []
        #保存左子节点
        stack = []
        cur_node = root
        pre_val = float('-inf')  # 不用-0x7fffffff，不保险
        while len(stack) > 0 or cur_node:
            #一直走到该子树的最左节点
            while cur_node != None:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            mid_list.append(cur_node.val)
            if cur_node.val <= pre_val:
                return False
            #记录最后一次的节点值
            pre_val = cur_node.val
            #如果有右节点则遍历右节点，即使为空
            cur_node = cur_node.right

        print(mid_list)

        #判断数组是否有序

        return result
