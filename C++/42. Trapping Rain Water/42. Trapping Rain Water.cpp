#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() <= 2)
            return 0;

        int l = 0;
        int r = l + 1;
        int area = 0;
        int temp_area = 0;

        while (r < height.size()) {
            if (height[l] <= height[r]) {
                area += temp_area + (height[l] * (r - l - 1));
                l = r;
                r = l + 1;
                temp_area = 0;
                continue;
            }
            temp_area -= height[r];
            r++;
        }
        int max_index = l;
        r = height.size() - 1;
        l = r - 1;
        temp_area = 0;

        while (l >= max_index) {
            if (height[l] >= height[r]) {
                area += temp_area + (height[r] * (r - l - 1));
                r = l;
                l = r - 1;
                temp_area = 0;
                continue;
            }
            temp_area -= height[l];
            l--;
        }

        return area;
    }
};

int main() {
    vector<int> vec = {4,2,3,1};
    cout << Solution().trap(vec);
    return 0;
}