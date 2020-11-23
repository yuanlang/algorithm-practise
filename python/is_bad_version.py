#!/usr/bin/python
# -*- coding: GBK -*-

# 第一个错误的版本
# 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

# 你可以通过调用?bool isBadVersion(version)?接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

# 示例:

# 给定 n = 5，并且 version = 4 是第一个错误的版本。

# 调用 isBadVersion(3) -> false
# 调用 isBadVersion(5)?-> true
# 调用 isBadVersion(4)?-> true

# 所以，4 是第一个错误的版本。?

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnto1s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

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
        #处理第一个版本就为True的情况
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
            # ! 防止整数溢出
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
