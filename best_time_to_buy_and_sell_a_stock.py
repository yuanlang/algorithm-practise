#!/usr/bin/python
# -*- coding: GBK -*-

# 121. 买卖股票的最佳时机
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

# 注意：你不能在买入股票前卖出股票。


# 示例 1:

# 输入: [7, 1, 5, 3, 6, 4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# 注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2:

# 输入: [7, 6, 4, 3, 1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

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
