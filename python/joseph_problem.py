#!/usr/bin/python
# -*- coding: GBK -*-

from typing import List


class LinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
    def change(self, node_data):
        self.data = node_data

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def insert_to_tail(self, data):
        new_node = LinkedListNode(data)
        if self.head == None:
            self.head = new_node
            self.len = 1
            return
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
        self.len += 1
        return
        
    def print(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next
        print()

    def length(self):
        return self.len

class Solution:
    def joseph_loop(self, nums: List[int], m: int) -> List[int]:
        result_list = []
        n = len(nums)
        # id, code, delete state
        processs_list = []
        for i in range(n):
            processs_list.append([i + 1, nums[i], False])
            
        cur_index = 0
        remain_num = len(nums)
        while remain_num > 0:
            i = 0
            while i < m:
                #�����Ѿ����ΪDelete True�Ľڵ�
                if processs_list[cur_index][2] != True:
                    i += 1
                    #����ڵ����ﵽm���Ͳ������ƶ���ǰ�ڵ���
                    if i == m:
                        break

                cur_index += 1

                # ���������processs_list���ȣ���ת
                if cur_index == len(processs_list):
                    cur_index = 0

            #��ǵ�ǰ�ڵ�Ϊdelete
            processs_list[cur_index][2] = True
            result_list.append(processs_list[cur_index][0])
            m = processs_list[cur_index][1]
            #������ǰ�ڵ�
            cur_index += 1
            # ���������processs_list���ȣ���ת
            if cur_index == len(processs_list):
                cur_index = 0

            remain_num -= 1

        return result_list

    def joseph_linked_list(self, nums: List[int], m: int) -> List[int]:
        link_list = LinkedList()
        for i in range(len(nums)):
            link_list.insert_to_tail([i+1, nums[i], False])
        # link_list.print()

        result_list = []
        remain_num = link_list.length()
        cur_node = link_list.head
        while remain_num > 0:
            i = 0
            while i < m:
                #�����Ѿ����ΪDelete True�Ľڵ�
                if cur_node.data[2] != True:
                    i += 1
                    #����ڵ����ﵽm���Ͳ������ƶ���ǰ�ڵ���
                    if i == m:
                        break

                cur_node = cur_node.next

                # ���������processs_list���ȣ���ת
                if cur_node == None:
                    cur_node = link_list.head

            #��ǵ�ǰ�ڵ�Ϊdelete
            cur_node.data[2] = True
            result_list.append(cur_node.data[0])
            # print(result_list)
            m = cur_node.data[1]
            #������ǰ�ڵ�
            cur_node = cur_node.next
            # ���������processs_list���ȣ���ת
            if cur_node == None:
                cur_node = link_list.head

            remain_num -= 1

        return result_list

if __name__ == "__main__":
    s = Solution()
    l = [3, 1, 7, 2, 4, 8, 4]
    m = 6
    print(s.joseph_loop(l, m))
    m = 8
    print(s.joseph_loop(l, m))

    m = 6
    print(s.joseph_linked_list(l, m))
    m = 8
    print(s.joseph_linked_list(l, m))
