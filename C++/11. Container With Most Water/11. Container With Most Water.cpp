#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int area = 0;
        while (l != r) {
            area = max(min(height[l], height[r]) * (r - l), area);
            if (height[l] > height[r])
                r--;
            else
                l++;
        }
        return area;
    }
};

int main() {
    vector<int> vec = {1,8,6,2,5,4,8,3,7};
    cout << Solution().maxArea(vec);
    return 0;
}