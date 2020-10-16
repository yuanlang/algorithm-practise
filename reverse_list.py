#!/usr/bin/python
# -*- coding: GBK -*-

# ��ת����
# ��תһ��������

# ʾ��:

# ����: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
# ���: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
# ����:
# ����Ե�����ݹ�ط�ת�������ܷ������ַ����������⣿

# ���ߣ�����(LeetCode)
# ���ӣ�https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnnhm6/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

from typing import List

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(nums: List) -> ListNode:
    n = len(nums)
    head = None
    cur_node = head
    pre_node = head
    for i in range(n):
        cur_node = ListNode(nums[i])
        if head == None:
            head = cur_node
            pre_node = cur_node
        else:
            pre_node.next = cur_node
        pre_node = cur_node
    return head

def print_list_node(l: ListNode):
    while l is not None:
        print(l.val, end=', ')
        l = l.next
    print()

class Solution:
    def reverseListRecursive(self, head: ListNode) -> ListNode:
        # if head's next is none, return this node
        # else, this node's next point to the previous node
        if head == None or head.next == None:
            return head

        new_head = self.reverseList(head.next)
        cur_node = new_head
        while cur_node.next != None:
            cur_node = cur_node.next
        head.next = None
        cur_node.next = head
        # print(new_head)
        return new_head

    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        cur_node = head
        node_list = []

        while cur_node.next != None:
            # cur_node.next = None
            node_list.append(cur_node)
            cur_node = cur_node.next
        # print(node_list)
        new_head = cur_node
        while len(node_list) > 0:
            # print(node_list)
            pop_node = node_list.pop()
            pop_node.next = None
            cur_node.next = pop_node
            cur_node = pop_node

        return new_head


if __name__ == "__main__":
    # expect: [3, 2, 1]
    s = Solution()
    l1 = create_linked_list([1, 2, 3])
    print_list_node(l1)
    print_list_node(s.reverseList(l1))
