function twoSum(nums: number[], target: number): number[] {
    let hash: { [key: number]: number } = {};
    
    for (let i = 0; i < nums.length; i++) {
        let subtracted = target - nums[i];

        if (subtracted in hash) 
            return [hash[subtracted], i];

        hash[nums[i]] = i;
    }
    return [];
};

console.log(twoSum([2,7,11,15], 9));