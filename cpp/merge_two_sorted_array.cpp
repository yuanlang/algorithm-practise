#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution
{
public:
    //思路：
    // 从后往前扫描两个数组，对于比较出来的较大值插入到A数组的后面
    void merge(int A[], int m, int B[], int n)
    {
        //如果数组B为空，则直接退出
        if (n == 0)
        {
            return;
        }

        int cur_a = m - 1;
        int cur_b = n - 1;
        for (int i = m + n - 1; i >= 0; i--)
        {
            // 如果一个数组提前结束
            if (cur_a < 0 || cur_b < 0)
            {
                break;
            }
            if (A[cur_a] > B[cur_b])
            {
                A[i] = A[cur_a--];
            }
            else
            {
                A[i] = B[cur_b--];
            }
        }

        //只考虑拷贝数组B中剩余部分
        if (cur_b >= 0)
        {
            for (int i = 0; i < cur_b + 1; i++)
            {
                A[i] = B[i];
            }
        }
    }
};

//两个数组大小穿插
void testcase1() {
    int a1[6] = {1, 4, 19};
    int a2[] = {2, 8, 9};
    Solution s;
    s.merge(a1, 3, a2, 3);
    for (size_t i = 0; i < 6; i++)
    {
        cout << a1[i] << " ";
    }
    cout << endl;
}

//数组A元素都大于数组B
void testcase2()
{
    int a1[6] = {10, 14, 19};
    int a2[] = {2, 8, 9};
    Solution s;
    s.merge(a1, 3, a2, 3);
    for (size_t i = 0; i < 6; i++)
    {
        cout << a1[i] << " ";
    }
    cout << endl;
}

//数组B元素都大于数组A
void testcase3()
{
    int a1[6] = {2, 8, 9};
    int a2[] = {10, 14, 19};
    Solution s;
    s.merge(a1, 3, a2, 3);
    for (size_t i = 0; i < 6; i++)
    {
        cout << a1[i] << " ";
    }
    cout << endl;
}

//数组A为空
void testcase4()
{
    int a1[3] = {};
    int a2[] = {10, 14, 19};
    Solution s;
    s.merge(a1, 0, a2, 3);
    for (size_t i = 0; i < 3; i++)
    {
        cout << a1[i] << " ";
    }
    cout << endl;
}

//数组B为空
void testcase5()
{
    int a1[3] = {10, 14, 19};
    int a2[] = {};
    Solution s;
    s.merge(a1, 3, a2, 0);
    for (size_t i = 0; i < 3; i++)
    {
        cout << a1[i] << " ";
    }
    cout << endl;
}

//数组A和B都为空
void testcase6()
{
    int a1[3] = {};
    int a2[] = {};
    Solution s;
    s.merge(a1, 3, a2, 0);
    for (size_t i = 0; i < 0; i++)
    {
        cout << a1[i] << " ";
    }
    cout << endl;
}

//数组A和B都只有一个元素
void testcase7()
{
    int a1[2] = {10};
    int a2[] = {1};
    Solution s;
    s.merge(a1, 1, a2, 1);
    for (size_t i = 0; i < 2; i++)
    {
        cout << a1[i] << " ";
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
    testcase6();
    testcase7();

    return 0;
}
