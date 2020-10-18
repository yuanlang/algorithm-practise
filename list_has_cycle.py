#!/usr/bin/python
# -*- coding: GBK -*-

# ��������
# ����һ�������ж��������Ƿ��л���

# �����������ĳ���ڵ㣬����ͨ���������� next ָ���ٴε���������д��ڻ��� Ϊ�˱�ʾ���������еĻ�������ʹ������ pos ����ʾ����β���ӵ������е�λ�ã������� 0 ��ʼ���� ��� pos �� - 1�����ڸ�������û�л���ע�⣺pos ����Ϊ�������д��ݣ�������Ϊ�˱�ʶ�����ʵ�������

# ��������д��ڻ����򷵻� true �� ���򣬷��� false ��

# ?

# ���ף�

# ������ O(1)�������������ڴ�����������

# ?

# ʾ�� 1��


# ���룺head = [3, 2, 0, -4], pos = 1
# �����true
# ���ͣ���������һ��������β�����ӵ��ڶ����ڵ㡣
# ʾ��?2��


# ���룺head = [1, 2], pos = 0
# �����true
# ���ͣ���������һ��������β�����ӵ���һ���ڵ㡣
# ʾ�� 3��


# ���룺head = [1], pos = -1
# �����false
# ���ͣ�������û�л���
# ?

# ��ʾ��

# �����нڵ����Ŀ��Χ��[0, 104]
# -105 <= Node.val <= 105
# pos Ϊ - 1 ���������е�һ�� ��Ч���� ��

# ���ߣ�����(LeetCode)
# ���ӣ�https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnwzei/
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
    def hasCycle(self, head: ListNode) -> bool:
        #��Dict KeyΪ�ڵ�ֵ��ValueΪ�ڵ�����
        cur_node = head
        temp_dict = {}
        while cur_node != None:
            if cur_node.next != None and cur_node.next.val in temp_dict:
                for item in temp_dict[cur_node.next.val]:
                    if item == cur_node.next:
                        return True
            if cur_node.val not in temp_dict:
                temp_dict[cur_node.val] = []
            temp_dict[cur_node.val].append(cur_node)
            cur_node = cur_node.next
        return False

#������ԣ�����Ҫ���ݵڶ�������������״����
