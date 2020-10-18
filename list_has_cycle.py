#!/usr/bin/python
# -*- coding: GBK -*-

# 环形链表
# 给定一个链表，判断链表中是否有环。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 - 1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

# 如果链表中存在环，则返回 true 。 否则，返回 false 。

# ?

# 进阶：

# 你能用 O(1)（即，常量）内存解决此问题吗？

# ?

# 示例 1：


# 输入：head = [3, 2, 0, -4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 示例?2：


# 输入：head = [1, 2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 示例 3：


# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
# ?

# 提示：

# 链表中节点的数目范围是[0, 104]
# -105 <= Node.val <= 105
# pos 为 - 1 或者链表中的一个 有效索引 。

# 作者：力扣(LeetCode)
# 链接：https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnwzei/
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
    def hasCycle(self, head: ListNode) -> bool:
        #用Dict Key为节点值，Value为节点数据
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

#如需测试，则需要根据第二个参数构建环状链表
