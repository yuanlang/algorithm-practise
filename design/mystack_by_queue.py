#!/usr/bin/python
# -*- coding: GBK -*-

# 225. �ö���ʵ��ջ
# ʹ�ö���ʵ��ջ�����в�����

# push(x) -- Ԫ�� x ��ջ
# pop() -- �Ƴ�ջ��Ԫ��
# top() -- ��ȡջ��Ԫ��
# empty() -- ����ջ�Ƿ�Ϊ��
# ע��:

# ��ֻ��ʹ�ö��еĻ�������-- Ҳ���� push to back, peek/pop from front, size, �� is empty ��Щ�����ǺϷ��ġ�
# ����ʹ�õ�����Ҳ��֧�ֶ��С� �����ʹ�� list ���� deque��˫�˶��У���ģ��һ������ , ֻҪ�Ǳ�׼�Ķ��в������ɡ�
# ����Լ������в���������Ч�ģ�����, ��һ���յ�ջ������� pop ���� top ��������

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.stack) == 0


if __name__ == "__main__":
    # Your MyStack object will be instantiated and called as such:
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    param_2 = stack.top()
    print(param_2)
    param_3 = stack.pop()
    print(param_3)
    param_4 = stack.empty()
    print(param_4)
