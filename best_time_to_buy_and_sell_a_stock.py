#!/usr/bin/python
# -*- coding: GBK -*-

# 121. ������Ʊ�����ʱ��
# ����һ�����飬���ĵ� i ��Ԫ����һ֧������Ʊ�� i ��ļ۸�

# ��������ֻ�������һ�ʽ��ף������������һ֧��Ʊһ�Σ������һ���㷨�����������ܻ�ȡ���������

# ע�⣺�㲻���������Ʊǰ������Ʊ��


# ʾ�� 1:

# ����: [7, 1, 5, 3, 6, 4]
# ���: 5
# ����: �ڵ� 2 �죨��Ʊ�۸� = 1����ʱ�����룬�ڵ� 5 �죨��Ʊ�۸� = 6����ʱ��������������� = 6-1 = 5 ��
# ע���������� 7-1 = 6, ��Ϊ�����۸���Ҫ��������۸�ͬʱ���㲻��������ǰ������Ʊ��
# ʾ�� 2:

# ����: [7, 6, 4, 3, 1]
# ���: 0
# ����: �����������, û�н������, �����������Ϊ 0��

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        elif n == 2:
            return max(prices[1]-prices[0], 0)
        bestbuy = [prices[0], min(prices[:2])]
        bestsell = [-0xffffffff]
        if prices[1] < prices[0]:
            bestsell.append(-0xffffffff)
        else:
            bestsell.append(prices[1])
        profit = [0, max(prices[1]-prices[0], 0)]

        buypricechnage = False
        for i in range(2, n):
            bestbuy.append(min(bestbuy[-1], prices[i-1]))
            if bestbuy[-1] != bestbuy[-2]:
                buypricechnage = True
            if bestbuy[i] > prices[i] and bestsell[-1] < 0:
                bestsell.append(-0xffffffff)
            else:
                if buypricechnage == False:
                    bestsell.append(max(bestsell[-1], prices[i]))
                else:
                    bestsell.append(prices[i])
            profit.append(max(bestsell[-1] - bestbuy[-1], profit[-1]))
            buypricechnage = False
        print(bestbuy)
        print(bestsell)
        print(profit)
        return profit[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 4, 1, 2]))
    print(s.maxProfit([3, 2, 6, 5, 0, 3]))
    print(s.maxProfit([2, 1, 2, 0, 1]))
    print(s.maxProfit([2, 1, 2, 1, 0, 0, 1]))
    print(s.maxProfit([7, 5, 3, 6, 8, 6, 3, 4, 10, 1]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
