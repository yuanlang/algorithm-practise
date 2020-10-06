# С���������м�ѡ����һ�����̯λ��һά�������� staple �м�¼��ÿ����ʳ�ļ۸�һά�������� drinks �м�¼��ÿ�����ϵļ۸�С�۵ļƻ�ѡ��һ����ʳ��һ�����ϣ��һ��Ѳ����� x Ԫ���뷵��С�۹��ж����ֹ��򷽰���

# ע�⣺����Ҫ�� 1e9 + 7 (1000000007) Ϊ��ȡģ���磺�����ʼ���Ϊ��1000000008���뷵�� 1

# ʾ�� 1��

# ���룺staple = [10, 20, 5], drinks = [5, 5, 2], x = 15

# �����6

# ���ͣ�С���� 6 �ֹ��򷽰�����ѡ��ʳ����ѡ�����������ж�Ӧ���±�ֱ��ǣ�
# �� 1 �ַ�����staple[0] + drinks[0] = 10 + 5 = 15��
# �� 2 �ַ�����staple[0] + drinks[1] = 10 + 5 = 15��
# �� 3 �ַ�����staple[0] + drinks[2] = 10 + 2 = 12��
# �� 4 �ַ�����staple[2] + drinks[0] = 5 + 5 = 10��
# �� 5 �ַ�����staple[2] + drinks[1] = 5 + 5 = 10��
# �� 6 �ַ�����staple[2] + drinks[2] = 5 + 2 = 7��

# ʾ�� 2��

# ���룺staple = [2, 1, 1], drinks = [8, 9, 5, 1], x = 9

# �����8

# ���ͣ�С���� 8 �ֹ��򷽰�����ѡ��ʳ����ѡ�����������ж�Ӧ���±�ֱ��ǣ�
# �� 1 �ַ�����staple[0] + drinks[2] = 2 + 5 = 7��
# �� 2 �ַ�����staple[0] + drinks[3] = 2 + 1 = 3��
# �� 3 �ַ�����staple[1] + drinks[0] = 1 + 8 = 9��
# �� 4 �ַ�����staple[1] + drinks[2] = 1 + 5 = 6��
# �� 5 �ַ�����staple[1] + drinks[3] = 1 + 1 = 2��
# �� 6 �ַ�����staple[2] + drinks[0] = 1 + 8 = 9��
# �� 7 �ַ�����staple[2] + drinks[2] = 1 + 5 = 6��
# �� 8 �ַ�����staple[2] + drinks[3] = 1 + 1 = 2��

# ��ʾ��

# 1 <= staple.length <= 10 ^ 5
# 1 <= drinks.length <= 10 ^ 5
# 1 <= staple[i], drinks[i] <= 10 ^ 5
# 1 <= x <= 2*10 ^ 5

# ��Դ�����ۣ�LeetCode��
# ���ӣ�https: // leetcode-cn.com/problems/2vYnGI
# ����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������

class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        #�ȴӴ�С�����ҵ���һ������ģ�Ȼ��ʣ�µ�ֱ����Ӽ���
        sort_staple = sorted(staple, reverse=False)
        sort_drinks = sorted(drinks, reverse=True)
        # print(sort_staple)
        # print(sort_drinks)
        staple_len = len(sort_staple)
        drinks_len = len(sort_drinks)
        print(staple_len, drinks_len)
        ret = 0
        start = 0
        for s in sort_staple:
            # drink cost >= 1, then s cannot equal to x
            if s >= x:
                continue
            remain = x - s
            for j in range(start, drinks_len):
                if sort_drinks[j] <= remain:
                    start = j
                    ret += (drinks_len - j)
                    break
            # print(s, ret, start)
        return ret % (10 ** 9 + 7)
