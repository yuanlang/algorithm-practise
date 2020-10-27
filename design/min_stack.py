#!/usr/bin/python
# -*- coding: GBK -*-

# ��Сջ
# ���һ��֧�� push ��pop ��top �����������ڳ���ʱ���ڼ�������СԪ�ص�ջ��

# push(x) ���� ��Ԫ�� x ����ջ�С�
# pop()?���� ɾ��ջ����Ԫ�ء�
# top()?���� ��ȡջ��Ԫ�ء�
# getMin() ���� ����ջ�е���СԪ�ء�
# ?

# ʾ��:

# ���룺
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# �����
# [null,null,null,null,-3,null,0,-2]

# ���ͣ�
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> ���� -3.
# minStack.pop();
# minStack.top();      --> ���� 0.
# minStack.getMin();   --> ���� -2.

# ��ʾ��
# pop��top �� getMin ���������� �ǿ�ջ �ϵ��á�

# ���ߣ����� (LeetCode)
# ���ӣ�https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnkq37/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.smallest = float('inf')

    def push(self, x: int) -> None:
        # print("push", x)
        #������Сֵ
        if x < self.smallest:
            self.smallest = x
        self.stack.append(x)

    def pop(self) -> int:
        # print("pxop")
        cur = self.stack.pop()
        #������Сֵ����Ҫ�ر��עջΪ��ʱ�ĸ���
        if len(self.stack) == 0:
            self.smallest = float('inf')
        if self.stack.count(cur) == 0 and len(self.stack) > 0:
            temp_list = sorted(self.stack)
            self.smallest = temp_list[0]
            # print("update", self.smallest)

    def top(self) -> int:
        # print("top")
        return self.stack[-1]

    def getMin(self) -> int:
        # print("getMin")
        return self.smallest


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
