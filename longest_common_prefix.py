#!/usr/bin/python
# -*- coding: GBK -*-

# �����ǰ׺
# ��дһ�������������ַ��������е������ǰ׺��

# ��������ڹ���ǰ׺�����ؿ��ַ���?""��

# ʾ��?1:

# ����: ["flower","flow","flight"]
# ���: "fl"
# ʾ��?2:

# ����: ["dog","racecar","car"]
# ���: ""
# ����: ���벻���ڹ���ǰ׺��
# ˵��:


# ���ߣ����� (LeetCode)
# ���ӣ�https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnmav1/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

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
        # �ȱȽ�1��2�����ù���ǰ꡸������Ƚ�
        common = self.findCommonPrefixInTwoStr(strs[0], strs[1])
        for i in range(2, n):
            common = self.findCommonPrefixInTwoStr(common, strs[i])
        return common

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix(["ab", "a"]))
