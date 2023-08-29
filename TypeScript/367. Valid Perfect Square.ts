export {};

function isPerfectSquare(num: number): boolean {
    let start = 1;
    let end = num - 1;
    if (num === 1) return true
    while (start <= end) {
        let mid = Math.floor((start + end) / 2);
        if (mid * mid == num) return true;
        else if (mid * mid > num) end = mid - 1
        else start = mid + 1;
    }
    return false
};

console.log(isPerfectSquare(144));