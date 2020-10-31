#!/usr/bin/python
# -*- coding: GBK -*-

from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBSTv1(self, nums: List[int]) -> TreeNode:
        # ����������������ݹ鹹������������
        length = len(nums)
        if length == 0:
            return None
        if length == 1:
            root = TreeNode(nums[0])
            return root
        root_val = None
        mid = int(length / 2)
        root_val = nums[mid]
        left = mid - 1
        right = mid + 1
        root = TreeNode(root_val)
        root.left = self.sortedArrayToBST(nums[0:left+1])
        root.right = self.sortedArrayToBST(nums[right:length])
        return root

    # ����汾
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Helper�汾
        def helper(left, right):
            if left > right:
                return None

            #����ѡ���м�λ����ߵ�������Ϊ���ڵ�
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)

def levelOrder(root: TreeNode) -> List[List[int]]:
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

if __name__ == "__main__":
    s = Solution()
    l = []
    r = s.sortedArrayToBST(l)
    print(levelOrder(r))

    l = [1]
    r = s.sortedArrayToBST(l)
    print(levelOrder(r))

    l = [-3, 1, 4]
    r = s.sortedArrayToBST(l)
    print(levelOrder(r))

    l = [-10, -3, 0, 5, 9]
    r = s.sortedArrayToBST(l)
    print(levelOrder(r))
