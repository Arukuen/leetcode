function findMaxAverage(nums: number[], k: number): number {
    let currentSum = 0;
    
    // Initial
    for (let i = 0; i < k; i++) {
        currentSum += nums[i];
    }
    let maxAve = currentSum / k;

    for (let i = k; i < nums.length; i++) {
        currentSum -= nums[i-k]
        currentSum += nums[i];
        maxAve = Math.max(maxAve, currentSum / k);
    }
    return maxAve;
};

console.log(findMaxAverage([1,12,-5,-6,50,3], 4));