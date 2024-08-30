function containsDuplicate(nums: number[]): boolean {
    const hash: {[key: number]: boolean} = {};

    for (const n of nums) {
        if (!(n in hash)) {
            hash[n] = true
        }
        else {
            return true
        }
    }
    return false;
};

console.log(containsDuplicate([1,2,3]))