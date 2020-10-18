#!/usr/bin/python
# -*- coding: GBK -*-

# 回文链表
# 请判断一个链表是否为回文链表。

# 示例 1:

# 输入: 1 -> 2
# 输出: false
# 示例 2:

# 输入: 1 -> 2 -> 2 -> 1
# 输出: true
# 进阶：
# 你能否用?O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# 作者：力扣(LeetCode)
# 链接：https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnv1oc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

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
        
        #把链表从slow位置断开
        # print_list_node(slow)
        # print_list_node(fast)
        pre_slow.next = None
        print_list_node(head)

        #对Slow位置后的链表进行反转
        cur_node = slow
        pre_node = None
        while cur_node != None:
            #先保存下一个节点
            next_node = cur_node.next
            #如果是第一个节点，则修改当前节点的next为空
            if pre_node == None:
                cur_node.next = None
            else:
                cur_node.next = pre_node
            #修改pre和 cur的值
            pre_node = cur_node
            cur_node = next_node
        
        new_head = pre_node
        
        # 从两个头开始，逐个比较，不相等则返回False
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
