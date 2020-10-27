#!/usr/bin/python
# -*- coding: GBK -*-

# 最小栈
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

# push(x) —— 将元素 x 推入栈中。
# pop()?—— 删除栈顶的元素。
# top()?—— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
# ?

# 示例:

# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# 输出：
# [null,null,null,null,-3,null,0,-2]

# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

# 提示：
# pop、top 和 getMin 操作总是在 非空栈 上调用。

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnkq37/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.smallest = float('inf')

    def push(self, x: int) -> None:
        # print("push", x)
        #更新最小值
        if x < self.smallest:
            self.smallest = x
        self.stack.append(x)

    def pop(self) -> int:
        # print("pxop")
        cur = self.stack.pop()
        #更新最小值，需要特别关注栈为空时的更新
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
