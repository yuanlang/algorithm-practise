#!/usr/bin/python
# -*- coding: GBK -*-

# �������
# ����һ�������� n��1 ��?n?�� 30�������������еĵ� n �

# ע�⣺���������е�ÿһ���ʾΪһ���ַ�����

# ��������С���һ���������У������� 1 ��ʼ�������е�ÿһ��Ƕ�ǰһ���������ǰ�������£�

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# ��һ�������� 1

# ����ǰһ�������� 1 �� ��һ�� 1 �������� 11

# ����ǰһ�������� 11 �� ������ 1 �� ������ 21

# ����ǰһ�������� 21 �� ��һ�� 2 һ�� 1 �� ������ 1211

# ����ǰһ�������� 1211 �� ��һ�� 1 һ�� 2 ���� 1 �� ������ 111221

# ?

# ʾ��?1:

# ����: 1
# ���: "1"
# ���ͣ�����һ������������

# ʾ�� 2:

# ����: 4
# ���: "1211"
# ���ͣ��� n = 3 ʱ�������� "21"������������ "2" �� "1" ���飬"2" ���Զ��� "12"��Ҳ���ǳ���Ƶ�� = 1 �� ֵ = 2������ "1" ���Զ��� "11"�����Դ��� "12" �� "11" �����һ��Ҳ���� "1211"��

# ���ߣ�����(LeetCode)
# ���ӣ�https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnpvdm/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

class Solution:
    def countAndSay(self, n: int) -> str:
        result = []
        if n == 1:
            return "1"
        result.append(str(1))
        for _i in range(1, n):
            temp = str(result[-1])
            # print(temp)
            pre = ''
            count = 0
            ret = ''
            for c in temp:
                # c change in the middle
                if c != pre and pre != '':
                    ret += str(count) + pre
                    count = 1
                else:
                    count += 1
                pre = c
            # process the last char
            ret += str(count) + temp[-1]
            result.append(ret)

        return result[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(1))
    print(s.countAndSay(2))
    print(s.countAndSay(3))
    print(s.countAndSay(4))
    print(s.countAndSay(5))
    print(s.countAndSay(6))
