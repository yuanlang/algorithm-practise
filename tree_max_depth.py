#!/usr/bin/python
# -*- coding: GBK -*-

# 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。

# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

# 说明: 叶子节点是指没有子节点的节点。

# 示例：
# 给定二叉树[3, 9, 20, null, null, 15, 7]，

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度?3 。

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnd69e/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 非递归解法
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
            # 访问当前节点
            max_depth = max(cur_depth, max_depth)
            if cur_node.left != None:
                node_queue.append(cur_node.left)
                depth_queue.append(cur_depth + 1)
            if cur_node.right != None:
                node_queue.append(cur_node.right)
                depth_queue.append(cur_depth + 1)
            #每次取队列尾
            cur_node = node_queue[0]
            del(node_queue[0])
            cur_depth = depth_queue[0]
            del(depth_queue[0])

        return max_depth

    # 递归解法
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        max_depth = 0
        #如果为叶子节点，则返回深度为1
        if root.left == None and root.right == None:
            return 1
        if root.left != None:
            max_depth = max(max_depth, 1 + self.maxDepth(root.left))
        if root.right != None:
            max_depth = max(max_depth, 1 + self.maxDepth(root.right))

        return max_depth
