function removeDuplicates(nums: number[]): number {
    let slow = 1;
    for (let fast = 1; fast < nums.length; fast++) {
        if (nums[fast] !== nums[fast-1]) {
            nums[slow] = nums[fast];
            slow++;
        }
    }
    return slow;
};


console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]));