#!/usr/bin/python
# -*- coding: GBK -*-

# �ϲ�������������
# ��������������ϲ�Ϊһ���µ� ���� �������ء���������ͨ��ƴ�Ӹ�����������������нڵ���ɵġ�?

# ?

# ʾ����

# ���룺1 -> 2 -> 4, 1 -> 3 -> 4
# �����1 -> 1 -> 2 -> 3 -> 4 -> 4

# ���ߣ�����(LeetCode)
# ���ӣ�https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnnbp2/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val  = x
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # ������ָ���Ӧ��������ĵ�ǰλ�ã�ֱ��nextΪ��Ϊֹ
        cur_l1_node = l1
        cur_l2_node = l2
        new_list_head = None
        cur_new_list = None
        pre_new_list = None
        while cur_l1_node != None and cur_l2_node != None:
            #�Ƚϵ�ǰ�����ڵ��ֵ��С��д��������
            if cur_l1_node.val > cur_l2_node.val:
                value = cur_l2_node.val
                cur_l2_node = cur_l2_node.next
            else:
                value = cur_l1_node.val
                cur_l1_node = cur_l1_node.next
            cur_new_list = ListNode(value)
            if new_list_head == None:
                new_list_head = cur_new_list
            else:
                pre_new_list.next = cur_new_list
            pre_new_list = cur_new_list
            # print(new_list_head)
        
        remain_list_node = None
        if cur_l1_node != None:
            remain_list_node = cur_l1_node
        if cur_l2_node != None:
            remain_list_node = cur_l2_node

        while remain_list_node != None:
            cur_new_list = ListNode(remain_list_node.val)
            if new_list_head == None:
                new_list_head = cur_new_list
                pre_new_list = cur_new_list
            else:
                pre_new_list.next = cur_new_list
            pre_new_list = cur_new_list
            remain_list_node = remain_list_node.next

        return new_list_head


if __name__ == "__main__":
    # expect: [1, 1,, 2, 3, 3, 4]
    s = Solution()
    l1 = create_linked_list([1, 2, 3])
    print_list_node(l1)
    l2 = create_linked_list([1, 3, 4])
    print_list_node(l2)
    print_list_node(s.mergeTwoLists(l1, l2))
