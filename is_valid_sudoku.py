#!/usr/bin/python
# -*- coding: GBK -*-

# 有效的数独
# 判断一个?9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

# 数字?1-9?在每一行只能出现一次。
# 数字?1-9?在每一列只能出现一次。
# 数字?1-9?在每一个以粗实线分隔的?3x3?宫内只能出现一次。


# 上图是一个部分填充的有效的数独。

# 数独部分空格内已填入了数字，空白格用?'.'?表示。

# 示例?1:

# 输入:
# [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]
# 输出: true
# 示例?2:

# 输入:
# [
#     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
# ? ["6", ".", ".", "1", "9", "5", ".", ".", "."],
# ? [".", "9", "8", ".", ".", ".", ".", "6", "."],
# ? ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
# ? ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
# ? ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
# ? [".", "6", ".", ".", ".", ".", "2", "8", "."],
# ? [".", ".", ".", "4", "1", "9", ".", ".", "5"],
# ? [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]
# 输出: false
# 解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
# 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
# 说明:

# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 给定数独序列只包含数字?1-9?和字符?'.'?。
# 给定数独永远是?9x9?形式的。

# 作者：力扣(LeetCode)
# 链接：https: // leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2f9gg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 横向
        for i in range(9):
            for num in range(1, 10):
                if board[i].count(str(num)) > 1:
                    return False
        #纵向
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(board[j][i])
            print(temp)
            for i in range(1, 10):
                if temp.count(str(i)) > 1:
                    return False

        # 3 x 3
        list_3 = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                list_3[int(j/3) + int(i / 3) * 3].append(board[i][j])
        print(list_3)
        for i in range(9):
            for num in range(1, 10):
                if list_3[i].count(str(num)) > 1:
                    return False

        return True


if __name__ == "__main__":
    s = Solution()
    l = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
        [".", "4", ".", "3", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "3", ".", ".", "1"],
        ["8", ".", ".", ".", ".", ".", ".", "2", "."],
        [".", ".", "2", ".", "7", ".", ".", ".", "."],
        [".", "1", "5", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "2", ".", ".", "."],
        [".", "2", ".", "9", ".", ".", ".", ".", "."],
        [".",".","4",".",".",".",".",".","."]]
    print(s.isValidSudoku(l))
