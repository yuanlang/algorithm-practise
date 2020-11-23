#!/usr/bin/python
# -*- coding: GBK -*-

# LCP 19. ��Ҷ�ղؼ�
# С�۳�ȥ���Σ�;���ռ���һЩ��Ҷ�ͻ�Ҷ����������ЩҶ�ӳ���������һ����Ҷ�ղؼ� leaves�� �ַ��� leaves ������Сд�ַ� r �� y�� �����ַ� r ��ʾһƬ��Ҷ���ַ� y ��ʾһƬ��Ҷ��
# ������������Ŀ��ǣ�С����Ҫ���ղؼ�����Ҷ�����е����ɡ��졢�ơ��졹�����֡�ÿ������Ҷ�������Բ���ȣ���������ڵ��� 1��ÿ�ε���������С�ۿ��Խ�һƬ��Ҷ�滻�ɻ�Ҷ���߽�һƬ��Ҷ�滻�ɺ�Ҷ������С��������Ҫ���ٴε����������ܽ���Ҷ�ղؼ�������ϡ�

# ʾ�� 1��

# ���룺leaves = "rrryyyrryyyrr"

# �����2

# ���ͣ��������Σ����м����Ƭ��Ҷ�滻�ɻ�Ҷ���õ� "rrryyyyyyyyrr"

# ʾ�� 2��

# ���룺leaves = "ryr"

# �����0

# ���ͣ��ѷ���Ҫ�󣬲���Ҫ�������

# ��ʾ��

# 3 <= leaves.length <= 10 ^ 5
# leaves ��ֻ�����ַ� 'r' ���ַ� 'y'

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
        # ���������������������
        # ȫ��Ϊ����Ҫ�Ĳ���
        # ǰ��Ϊ�����Ϊ����Ҫ�Ĳ���
        # ǰ��Ϊ�죬�м�Ϊ�ƣ����Ϊ��Ĳ���
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
