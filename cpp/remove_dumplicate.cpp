#include <iostream>
#include <vector>
#include <queue>

using namespace std;
class Solution {
public:
    //思路：双指针
    // 快指针，一个指针指向当前遍历的元素
    // 慢指针，另一个指向当前非重复元素的位置
    int removeDuplicates(vector<int> &nums) {
        //如果数组为空
        if (nums.size() == 0) {
            return 0;
        }

        // int count = 1; //直接从第二个元素开始，所以长度直接修改为1
        int j = 1; //指向当前不重复的元素位置
        int pre = nums[0];
        for (int i=1;i<nums.size();i++) {
            // cout << nums[i];
            // 只有当前元素不等于pre的情况下才处理
            if (nums[i] != pre) {
                // count++;
                nums[j] = nums[i];
                pre = nums[i];
                j++;
            }
        }
        // for (int i=j+1;i<nums.size();i++) {
        //     nums.pop_back();
        // }
        return j;
    }

    void printWithLength(const vector<int> &nums, int length) {
        for (int i = 0; i < length; i++)
        {
            cout << nums[i] << " ";
        }
        cout << endl;
    }

};

int main(int argc, char *argv[])
{
    vector<int> v = {1, 1, 2};
    Solution s;
    int length = s.removeDuplicates(v);
    s.printWithLength(v, length);
    return 0;
}