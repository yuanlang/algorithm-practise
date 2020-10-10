#!/usr/bin/python
# -*- coding: GBK -*-

# 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串?""。

# 示例?1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例?2:

# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:


# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnmav1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List

class Solution:
    def findCommonPrefixInTwoStr(self, str1: str, str2: str) -> str:
        ret = ''
        max_len = 0
        str1_len = len(str1)
        str2_len = len(str2)
        for i in range(min(str1_len, str2_len)):
            if str1[i] == str2[i]:
                ret += str1[i]
                max_len += 1
            else:
                break
        return ret

    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        if n == 1:
            return strs[0]
        # 先比较1和2，再用公共前辍跟其它比较
        common = self.findCommonPrefixInTwoStr(strs[0], strs[1])
        for i in range(2, n):
            common = self.findCommonPrefixInTwoStr(common, strs[i])
        return common

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix(["ab", "a"]))
