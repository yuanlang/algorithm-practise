#!/usr/bin/python
# -*- coding: GBK -*-

# 小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，一维整型数组 drinks 中记录了每种饮料的价格。小扣的计划选择一份主食和一款饮料，且花费不超过 x 元。请返回小扣共有多少种购买方案。

# 注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1

# 示例 1：

# 输入：staple = [10, 20, 5], drinks = [5, 5, 2], x = 15

# 输出：6

# 解释：小扣有 6 种购买方案，所选主食与所选饮料在数组中对应的下标分别是：
# 第 1 种方案：staple[0] + drinks[0] = 10 + 5 = 15；
# 第 2 种方案：staple[0] + drinks[1] = 10 + 5 = 15；
# 第 3 种方案：staple[0] + drinks[2] = 10 + 2 = 12；
# 第 4 种方案：staple[2] + drinks[0] = 5 + 5 = 10；
# 第 5 种方案：staple[2] + drinks[1] = 5 + 5 = 10；
# 第 6 种方案：staple[2] + drinks[2] = 5 + 2 = 7。

# 示例 2：

# 输入：staple = [2, 1, 1], drinks = [8, 9, 5, 1], x = 9

# 输出：8

# 解释：小扣有 8 种购买方案，所选主食与所选饮料在数组中对应的下标分别是：
# 第 1 种方案：staple[0] + drinks[2] = 2 + 5 = 7；
# 第 2 种方案：staple[0] + drinks[3] = 2 + 1 = 3；
# 第 3 种方案：staple[1] + drinks[0] = 1 + 8 = 9；
# 第 4 种方案：staple[1] + drinks[2] = 1 + 5 = 6；
# 第 5 种方案：staple[1] + drinks[3] = 1 + 1 = 2；
# 第 6 种方案：staple[2] + drinks[0] = 1 + 8 = 9；
# 第 7 种方案：staple[2] + drinks[2] = 1 + 5 = 6；
# 第 8 种方案：staple[2] + drinks[3] = 1 + 1 = 2；

# 提示：

# 1 <= staple.length <= 10 ^ 5
# 1 <= drinks.length <= 10 ^ 5
# 1 <= staple[i], drinks[i] <= 10 ^ 5
# 1 <= x <= 2*10 ^ 5

# 来源：力扣（LeetCode）
# 链接：https: // leetcode-cn.com/problems/2vYnGI
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        #先从大到小排序，找到第一个满足的，然后剩下的直接相加即可
        sort_staple = sorted(staple, reverse=False)
        sort_drinks = sorted(drinks, reverse=True)
        # print(sort_staple)
        # print(sort_drinks)
        staple_len = len(sort_staple)
        drinks_len = len(sort_drinks)
        print(staple_len, drinks_len)
        ret = 0
        start = 0
        for s in sort_staple:
            # drink cost >= 1, then s cannot equal to x
            if s >= x:
                continue
            remain = x - s
            for j in range(start, drinks_len):
                if sort_drinks[j] <= remain:
                    start = j
                    ret += (drinks_len - j)
                    break
            # print(s, ret, start)
        return ret % (10 ** 9 + 7)
