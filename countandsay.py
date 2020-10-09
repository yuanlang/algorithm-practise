#!/usr/bin/python
# -*- coding: GBK -*-

# 外观数列
# 给定一个正整数 n（1 ≤?n?≤ 30），输出外观数列的第 n 项。

# 注意：整数序列中的每一项将表示为一个字符串。

# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 第一项是数字 1

# 描述前一项，这个数是 1 即 “一个 1 ”，记作 11

# 描述前一项，这个数是 11 即 “两个 1 ” ，记作 21

# 描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211

# 描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221

# ?

# 示例?1:

# 输入: 1
# 输出: "1"
# 解释：这是一个基本样例。

# 示例 2:

# 输入: 4
# 输出: "1211"
# 解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。

# 作者：力扣(LeetCode)
# 链接：https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnpvdm/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

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
