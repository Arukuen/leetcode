#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (target < nums[mid]) 
                right = mid - 1;
            else if (target > nums[mid])
                left = mid + 1;
            else
                return mid;
        }
        return left;
    }
};

int main() {
    vector<int> vec = {1,3,5,6};
    cout << Solution().searchInsert(vec, 7);
    return 0;
}