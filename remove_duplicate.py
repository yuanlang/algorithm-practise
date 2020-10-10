#!/usr/bin/python
# -*- coding: GBK -*-

# ɾ�����������е��ظ���
# ����һ���������飬����Ҫ�� ԭ�� ɾ���ظ����ֵ�Ԫ�أ�ʹ��ÿ��Ԫ��ֻ����һ�Σ������Ƴ���������³��ȡ�

# ��Ҫʹ�ö��������ռ䣬������� ԭ�� �޸��������� ����ʹ�� O(1) ����ռ����������ɡ�

# ?

# ʾ��?1:

# �������� nums = [1, 1, 2],

# ����Ӧ�÷����µĳ��� 2, ����ԭ���� nums ��ǰ����Ԫ�ر��޸�Ϊ 1, 2��

# �㲻��Ҫ���������г����³��Ⱥ����Ԫ�ء�
# ʾ��?2:

# ���� nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],

# ����Ӧ�÷����µĳ��� 5, ����ԭ���� nums ��ǰ���Ԫ�ر��޸�Ϊ 0, 1, 2, 3, 4��

# �㲻��Ҫ���������г����³��Ⱥ����Ԫ�ء�
# ?

# ˵��:

# Ϊʲô������ֵ��������������Ĵ���������?

# ��ע�⣬�����������ԡ����á���ʽ���ݵģ�����ζ���ں������޸�����������ڵ������ǿɼ��ġ�

# ����������ڲ���������:

# // nums ���ԡ����á���ʽ���ݵġ�Ҳ����˵������ʵ�����κο���
# int len = removeDuplicates(nums)

# // �ں������޸�����������ڵ������ǿɼ��ġ�
# // ������ĺ������صĳ���, �����ӡ�������иó��ȷ�Χ�ڵ�����Ԫ�ء�
# for (int i=0
#      i < len
#      i++) {? ? print(nums[i])
#            }

# ���ߣ�����(LeetCode)
# ���ӣ�https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2gy9m/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        if n == 0:
            return 0
        pre = nums[0]
        count = 1
        index = 0
        for c in nums[1:]:
            if c == pre:
                del(nums[index])
                # print(nums, count, index, c, pre)
            else:
                count += 1
                index += 1
                pre = c


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))
    print(s.removeDuplicates([0, 0, 1, 1, 2, 2, 3, 3, 3]))
    print(s.removeDuplicates([]))
