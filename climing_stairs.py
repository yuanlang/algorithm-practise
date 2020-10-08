#!/usr/bin/python
# -*- coding: GBK -*-
# 
# 70. ��¥��
# ������������¥�ݡ���Ҫ n ������ܵ���¥����

# ÿ��������� 1 �� 2 ��̨�ס����ж����ֲ�ͬ�ķ�����������¥���أ�

# ע�⣺���� n ��һ����������

# ʾ�� 1��

# ���룺 2
# ����� 2
# ���ͣ� �����ַ�����������¥����
# 1.  1 �� + 1 ��
# 2.  2 ��
# ʾ�� 2��

# ���룺 3
# ����� 3
# ���ͣ� �����ַ�����������¥����
# 1.  1 �� + 1 �� + 1 ��
# 2.  1 �� + 2 ��
# 3.  2 �� + 1 ��

class Solution:
    cache = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            self.cache[1] = 1
            return 1
        if n == 2:
            self.cache[2] = 2
            return 2
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.cache[n]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStairs(5))
    print(s.climbStairs(6))
    print(s.climbStairs(60))
