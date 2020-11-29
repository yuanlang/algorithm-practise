#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution
{
public:
    //˼·��
    // �Ӻ���ǰɨ���������飬���ڱȽϳ����Ľϴ�ֵ���뵽A����ĺ���
    void merge(int A[], int m, int B[], int n)
    {
        //�������BΪ�գ���ֱ���˳�
        if (n == 0)
        {
            return;
        }

        int cur_a = m - 1;
        int cur_b = n - 1;
        for (int i = m + n - 1; i >= 0; i--)
        {
            // ���һ��������ǰ����
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

        //ֻ���ǿ�������B��ʣ�ಿ��
        if (cur_b >= 0)
        {
            for (int i = 0; i < cur_b + 1; i++)
            {
                A[i] = B[i];
            }
        }
    }
};

//���������С����
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

//����AԪ�ض���������B
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

//����BԪ�ض���������A
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

//����AΪ��
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

//����BΪ��
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

//����A��B��Ϊ��
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

//����A��B��ֻ��һ��Ԫ��
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
