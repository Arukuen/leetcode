function reverse(x: number): number {
    let res = 0;
    let is_negative = false;
    if (x < 0) {
        is_negative = true;
        x *= -1
    }

    let length = (x===0) ? 1 : Math.floor(Math.log10(x)) + 1;

    while (length > 0) {
        res += (x % 10) * Math.pow(10, length - 1);
        x = Math.floor(x / 10);
        length--;
    }
    
    if (is_negative)
        res = res * -1;
    if (res < -2147483648 || res > 2147483648 - 1)
        return 0;
    return res;
};

console.log(reverse(-2147483648));