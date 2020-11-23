#!/usr/bin/python
# -*- coding: GBK -*-

# LCP 19. 秋叶收藏集
# 小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
# 出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

# 示例 1：

# 输入：leaves = "rrryyyrryyyrr"

# 输出：2

# 解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

# 示例 2：

# 输入：leaves = "ryr"

# 输出：0

# 解释：已符合要求，不需要额外操作

# 提示：

# 3 <= leaves.length <= 10 ^ 5
# leaves 中只包含字符 'r' 和字符 'y'

class Solution:
    def minimumOperations_no_mem(self, leaves: str) -> int:
        str1_char_not = 'y'
        str2_char_not = 'r'
        str3_char_not = 'y'
        length = len(leaves)
        # pos1, the seprate between str1 and str2
        # pos2, the seprate between str2 and str3
        # length of each string need to bigger than 1
        ret = 10 ** 5
        pos1_start, pos1_end = 1, length - 2
        _pos2_start, pos2_end = 2, length - 1
        for i in range(pos1_start, pos1_end):
            for j in range(i+1, pos2_end):
                str1 = leaves[0:i]
                str2 = leaves[i:j]
                str3 = leaves[j:length]
                ret = min(ret, str1.count(str1_char_not) +
                          str2.count(str2_char_not) + str3.count(str3_char_not))
        return ret

    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        # 用三个数组来存三种情况
        # 全部为红需要的步数
        # 前面为红后面为黄需要的步数
        # 前面为红，中间为黄，最后为红的步数
        dp = [[float('inf'), float('inf'), float('inf')] for _i in range(n)]
        if leaves[0] == 'r':
            dp[0][0] = 0
        else:
            dp[0][0] = 1

        for i in range(1, n):
            if leaves[i] == 'r':
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = dp[i-1][0] + 1

            if leaves[i] == 'y':
                dp[i][1] = min(dp[i-1][1], dp[i-1][0])
            else:
                dp[i][1] = min(dp[i-1][1] + 1, dp[i-1][0] + 1)
            
            if i >= 2:
                if leaves[i] == 'r':
                    dp[i][2] = min(dp[i-1][2], dp[i-1][1])
                else:
                    dp[i][2] = min(dp[i-1][2] + 1, dp[i-1][1] + 1)
        
        print([s for s in leaves])
        print([str(i[0]) for i in dp])
        print([str(i[1]) for i in dp])
        print([str(i[2]) for i in dp])

        return dp[n - 1][2]
        
if __name__ == "__main__":
    s = Solution()
    print(s.minimumOperations("rrryyyrryyyrr"))
    print(s.minimumOperations("ryr"))
