#!/usr/bin/python
# -*- coding: GBK -*-

# ��������
# ���ж�һ�������Ƿ�Ϊ��������

# ʾ�� 1:

# ����: 1 -> 2
# ���: false
# ʾ�� 2:

# ����: 1 -> 2 -> 2 -> 1
# ���: true
# ���ף�
# ���ܷ���?O(n) ʱ�临�ӶȺ� O(1) �ռ临�ӶȽ�����⣿

# ���ߣ�����(LeetCode)
# ���ӣ�https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnv1oc/
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
    def isPalindrome(self, head: ListNode) -> bool:
        # if the list has zero or one element, return ture
        if head == None or head.next == None:
            return True

        fast = head
        slow = head
        pre_slow = head

        while fast != None and fast.next != None and slow != None:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        #�������slowλ�öϿ�
        # print_list_node(slow)
        # print_list_node(fast)
        pre_slow.next = None
        print_list_node(head)

        #��Slowλ�ú��������з�ת
        cur_node = slow
        pre_node = None
        while cur_node != None:
            #�ȱ�����һ���ڵ�
            next_node = cur_node.next
            #����ǵ�һ���ڵ㣬���޸ĵ�ǰ�ڵ��nextΪ��
            if pre_node == None:
                cur_node.next = None
            else:
                cur_node.next = pre_node
            #�޸�pre�� cur��ֵ
            pre_node = cur_node
            cur_node = next_node
        
        new_head = pre_node
        
        # ������ͷ��ʼ������Ƚϣ�������򷵻�False
        print_list_node(head)
        print_list_node(new_head)

        cur_old_node = head
        cur_new_node = new_head
        while cur_old_node != None and cur_old_node != None:
            if cur_old_node.val != cur_new_node.val:
                return False
            cur_old_node = cur_old_node.next
            cur_new_node = cur_new_node.next

        return True
            

if __name__ == "__main__":
    # expect: True
    s = Solution()
    l1 = create_linked_list([])
    print_list_node(l1)
    print(s.isPalindrome(l1))

    # expect: True
    s = Solution()
    l1 = create_linked_list([1])
    print_list_node(l1)
    print(s.isPalindrome(l1))

    # expect: True
    s = Solution()
    l1 = create_linked_list([1, 2, 2, 1])
    print_list_node(l1)
    print(s.isPalindrome(l1))

    # expect: True
    s = Solution()
    l1 = create_linked_list([1, 2, 3, 2, 1])
    print_list_node(l1)
    print(s.isPalindrome(l1))

    # expect: True
    s = Solution()
    l1 = create_linked_list([1, 2, 3, 3, 2, 1])
    print_list_node(l1)
    print(s.isPalindrome(l1))

    # expect: False
    s = Solution()
    l1 = create_linked_list([1, 2])
    print_list_node(l1)
    print(s.isPalindrome(l1))

    # expect: False
    s = Solution()
    l1 = create_linked_list([1, 2, 3, 4, 2, 1])
    print_list_node(l1)
    print(s.isPalindrome(l1))
