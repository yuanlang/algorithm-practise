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
    // one circle approach
    void rotate(vector<int> &nums, int k)
    {
        const int length = nums.size();
        // �������Ϊ�գ�ֱ�ӷ���
        if (length == 0)
        {
            return;
        }

        k = k % length;
        int count = 0;
        for (size_t start = 0; count < length; start++)
        {
            // cout << "start = " << start << endl;
            // print(nums);
            int cur_pos = start;
            int prev = nums[start];
            do
            {
                int new_pos = (cur_pos + k) % length;
                int temp = nums[new_pos];
                nums[new_pos] = prev;
                cur_pos = new_pos;
                prev = temp;
                count++;
                // print(nums);
            } while (cur_pos != start);
        }
    }

    void print(const vector<int> &nums)
    {
        for (auto item : nums)
        {
            cout << item << " ";
        }
        cout << endl;
    }

    // brute force approach
    void rotatev1(vector<int> &nums, int k)
    {
        const int length = nums.size();
        // �������Ϊ�գ�ֱ�ӷ���
        if (length == 0)
        {
            return;
        }

        for (size_t i = 0; i < k; i++)
        {
            //ÿһ�ζ��������ڵ�һ��Ԫ�أ�Ȼ������ƶ������Ԫ��
            int temp = nums[0];
            for (size_t j = 1; j < length; j++)
            {
                nums[j - 1] = nums[j];
            }
            nums[length - 1] = temp;
        }
    }
};

//����������Ԫ��Ϊż����
void testcase1()
{
    const int length = 4;
    vector<int> a1 = {1, 4, 8, 19};
    Solution s;
    s.rotate(a1, 2);
    for (auto item : a1)
    {
        cout << item << " ";
    }
    cout << endl;
}

//����������Ԫ��Ϊ������
void testcase2()
{
    const int length = 5;
    vector<int> a1 = {1, 4, 8, 10, 19};
    Solution s;
    s.rotate(a1, 2);
    for (auto item : a1)
    {
        cout << item << " ";
    }
    cout << endl;
}

//�ƶ�0��
void testcase3()
{
    const int length = 3;
    vector<int> a1 = {1, 4, 19};
    Solution s;
    s.rotate(a1, 0);
    for (auto item : a1)
    {
        cout << item << " ";
    }
    cout << endl;
}

//�ƶ��Ĵ����������鳤��
void testcase4()
{
    const int length = 3;
    vector<int> a1 = {1, 4, 19};
    Solution s;
    s.rotate(a1, 3);
    for (auto item : a1)
    {
        cout << item << " ";
    }
    cout << endl;
}

// ���鳤��Ϊ0
void testcase5()
{
    vector<int> a1 = {};
    Solution s;
    s.rotate(a1, 3);
    for (auto item : a1)
    {
        cout << item << " ";
    }
    cout << endl;
}

int main(int argc, char *argv[])
{
    testcase1();
    testcase2();
    testcase3();
    testcase4();
    testcase5();

    return 0;
}
