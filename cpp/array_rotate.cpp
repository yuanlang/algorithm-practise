// ��ת����
// ����һ�����飬�������е�Ԫ�������ƶ�?k?��λ�ã�����?k?�ǷǸ�����

// ʾ�� 1 :
// ���� : [ 1, 2, 3, 4, 5, 6, 7 ] �� k = 3
// ��� : [ 5, 6, 7, 1, 2, 3, 4 ]
// ���� : ������ת 1 �� : [ 7, 1, 2, 3, 4, 5, 6 ]
// ������ת 2 �� : [ 6, 7, 1, 2, 3, 4, 5 ]
// ������ת 3 �� : [ 5, 6, 7, 1, 2, 3, 4 ]

// ʾ��?2 :
// ���� : [ -1, -100, 3, 99 ] �� k = 2
// ��� : [ 3, 99, -1, -100 ]
// ���� : ������ת 1 �� : [ 99, -1, -100, 3 ]
// ������ת 2 �� : [ 3, 99, -1, -100 ]

//˵�� :
// �������������Ľ�����������������ֲ�ͬ�ķ������Խ��������⡣
// Ҫ��ʹ�ÿռ临�Ӷ�Ϊ?O(1) ��?ԭ��?�㷨��

// ���ߣ�����(LeetCode)
// ���ӣ�https : //leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2skh7/
// ��Դ�����ۣ�LeetCode��
// ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
    }
};

//���������С����
void testcase1()
{
    const int length = 3;
    vector<int> a1 = {1, 4, 19};
    Solution s;
    s.rotate(a1, 1);
    for (auto item : a1)
    {
        cout << item << " ";
    }
    cout << endl;
}

int main(int argc, char *argv[])
{
    testcase1();

    return 0;
}
