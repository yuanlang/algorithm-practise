#include <iostream>
#include <vector>
#include <queue>

using namespace std;
class Solution {
public:
    //˼·��˫ָ��
    // ��ָ�룬һ��ָ��ָ��ǰ������Ԫ��
    // ��ָ�룬��һ��ָ��ǰ���ظ�Ԫ�ص�λ��
    int removeDuplicates(vector<int> &nums) {
        //�������Ϊ��
        if (nums.size() == 0) {
            return 0;
        }

        // int count = 1; //ֱ�Ӵӵڶ���Ԫ�ؿ�ʼ�����Գ���ֱ���޸�Ϊ1
        int j = 1; //ָ��ǰ���ظ���Ԫ��λ��
        int pre = nums[0];
        for (int i=1;i<nums.size();i++) {
            // cout << nums[i];
            // ֻ�е�ǰԪ�ز�����pre������²Ŵ���
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