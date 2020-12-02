// 旋转数组
// 给定一个数组，将数组中的元素向右移动?k?个位置，其中?k?是非负数。

// 示例 1 :
// 输入 : [ 1, 2, 3, 4, 5, 6, 7 ] 和 k = 3
// 输出 : [ 5, 6, 7, 1, 2, 3, 4 ]
// 解释 : 向右旋转 1 步 : [ 7, 1, 2, 3, 4, 5, 6 ]
// 向右旋转 2 步 : [ 6, 7, 1, 2, 3, 4, 5 ]
// 向右旋转 3 步 : [ 5, 6, 7, 1, 2, 3, 4 ]

// 示例?2 :
// 输入 : [ -1, -100, 3, 99 ] 和 k = 2
// 输出 : [ 3, 99, -1, -100 ]
// 解释 : 向右旋转 1 步 : [ 99, -1, -100, 3 ]
// 向右旋转 2 步 : [ 3, 99, -1, -100 ]

//说明 :
// 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
// 要求使用空间复杂度为?O(1) 的?原地?算法。

// 作者：力扣(LeetCode)
// 链接：https : //leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2skh7/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
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
        // 如果数组为空，直接返回
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
        // 如果数组为空，直接返回
        if (length == 0)
        {
            return;
        }

        for (size_t i = 0; i < k; i++)
        {
            //每一次都让它等于第一个元素，然后逐个移动后面的元素
            int temp = nums[0];
            for (size_t j = 1; j < length; j++)
            {
                nums[j - 1] = nums[j];
            }
            nums[length - 1] = temp;
        }
    }
};

//正常，数组元素为偶数个
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

//正常，数组元素为奇数个
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

//移动0次
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

//移动的次数等于数组长度
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

// 数组长度为0
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
