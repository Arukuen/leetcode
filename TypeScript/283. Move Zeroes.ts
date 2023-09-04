function moveZeroes(nums: number[]): number[] {
    let r = 1
    let l = 0
    while (r < nums.length) {
        if (nums[r] != 0 && nums[l] == 0) {
            nums[l] = nums[r];
            nums[r] = 0;
        }
        if (nums[l] != 0) {
            l++;
        }
        r++;
    }
    return nums;
};
console.log(moveZeroes([1,0,1]));