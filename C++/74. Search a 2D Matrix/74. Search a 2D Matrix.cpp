#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size();
        int col = matrix[0].size();
        int left = 0;
        int right = row * col - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            int guess = matrix[mid/col][mid%col];
            if (target < guess) 
                right = mid - 1;
            else if (target > guess)
                left = mid + 1;
            else
                return true;
        }
        return false;
    }
};

int main() {
    vector<vector<int>> vec = {{1,1}};
    cout << Solution().searchMatrix(vec, 13);
    return 0;
}