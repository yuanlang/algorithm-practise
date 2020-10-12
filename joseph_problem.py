#!/usr/bin/python
# -*- coding: GBK -*-

from typing import List

class Solution:
    def joseph_loop(self, nums: List[int], m: int) -> List[int]:
        result_list = []
        n = len(nums)
        # id, code, delete state
        processs_list = []
        for i in range(n):
            processs_list.append([i + 1, nums[i], False])
            
        cur_index = 0
        remain_num = len(nums)
        while remain_num > 0:
            i = 0
            while i < m:
                #跳过已经标记为Delete True的节点
                if processs_list[cur_index][2] != True:
                    i += 1
                    #如果节点数达到m，就不能再移动当前节点了
                    if i == m:
                        break

                cur_index += 1

                # 如果大于了processs_list长度，则反转
                if cur_index == len(processs_list):
                    cur_index = 0

            #标记当前节点为delete
            processs_list[cur_index][2] = True
            result_list.append(processs_list[cur_index][0])
            m = processs_list[cur_index][1]
            #跳过当前节点
            cur_index += 1
            # 如果大于了processs_list长度，则反转
            if cur_index == len(processs_list):
                cur_index = 0

            remain_num -= 1

        return result_list

if __name__ == "__main__":
    s = Solution()
    l = [3, 1, 7, 2, 4, 8, 4]
    m = 6
    print(s.joseph_loop(l, m))
