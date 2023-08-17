#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cheapest = 10000;
        int maximum = 0;
        for (auto& price: prices) {
            if (price < cheapest) {
                cheapest = price;
                continue;
            }
            if (price - cheapest > maximum) {
                maximum = price-cheapest;
            }
        }
        return maximum;
    }
};

int main() {
    vector<int> vec = {7,6,4,3,1};
    Solution().maxProfit(vec);
    return 0;
}