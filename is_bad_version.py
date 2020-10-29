#!/usr/bin/python
# -*- coding: GBK -*-

# ��һ������İ汾
# ���ǲ�Ʒ����Ŀǰ���ڴ���һ���Ŷӿ����µĲ�Ʒ�����ҵ��ǣ���Ĳ�Ʒ�����°汾û��ͨ��������⡣����ÿ���汾���ǻ���֮ǰ�İ汾�����ģ����Դ���İ汾֮������а汾���Ǵ�ġ�

# �������� n ���汾 [1, 2, ..., n]�������ҳ�����֮�����а汾����ĵ�һ������İ汾��

# �����ͨ������?bool isBadVersion(version)?�ӿ����жϰ汾�� version �Ƿ��ڵ�Ԫ�����г���ʵ��һ�����������ҵ�һ������İ汾����Ӧ�þ������ٶԵ��� API �Ĵ�����

# ʾ��:

# ���� n = 5������ version = 4 �ǵ�һ������İ汾��

# ���� isBadVersion(3) -> false
# ���� isBadVersion(5)?-> true
# ���� isBadVersion(4)?-> true

# ���ԣ�4 �ǵ�һ������İ汾��?

# ���ߣ����� (LeetCode)
# ���ӣ�https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnto1s/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer

class Solution:
    def __init__(self):
        self.badVersion = None

    def setBadVersion(self, version):
        self.badVersion = version

    def isBadVersion(self, version):
        if version < self.badVersion:
            return False
        return True

    def firstBadVersionv1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        #�����һ���汾��ΪTrue�����
        if self.isBadVersion(1):
            return 1
        step = n
        cur_version = n
        while step > 0:
            cur_result = self.isBadVersion(cur_version)
            # print(cur_version, cur_result)
            step = int(step / 2)
            if cur_result == True:
                if self.isBadVersion(cur_version - 1) == False:
                    return cur_version
                cur_version = cur_version - step
            else:
                if self.isBadVersion(cur_version + 1) == True:
                    return cur_version + 1
                cur_version = cur_version + step

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            # ! ��ֹ�������
            mid = left + int((right - left) / 2)
            cur_result = self.isBadVersion(mid)
            if cur_result == True:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    s = Solution()
    s.setBadVersion(4)
    assert 4 == s.firstBadVersion(5)

    s.setBadVersion(20)
    assert 20 == s.firstBadVersion(30)

    s.setBadVersion(30)
    assert 30 == s.firstBadVersion(30)
