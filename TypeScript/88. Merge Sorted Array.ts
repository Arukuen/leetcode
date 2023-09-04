function merge(nums1: number[], m: number, nums2: number[], n: number): number[] {
    let mi = m-1;
    let ni = n-1;
    let r = n + m -1;
    while (r >= 0) {
        if (ni === -1 || nums1[mi] > nums2[ni]) {
            nums1[r] = nums1[mi];
            mi--;
        }
        else if (mi === -1 || nums1[mi] <= nums2[ni]) {
            nums1[r] = nums2[ni];
            ni--;
        }
        r--;
    }
    return nums1;
};


console.log(merge([0], 0, [1], 1));