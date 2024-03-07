function intToRoman(num: number): string {
    let hash: {[key: number]: string} = {
        1:    'I',
        4:    'IV',
        5:    'V',
        9:    'IX',
       10:    'X',
       40:    'XL',
       50:    'L',
       90:    'XC',
      100:    'C',
      400:    'CD',
      500:    'D',
      900:    'CM',
     1000:    'M'
    }
    let val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    let i = 0;
    let res = '';
    while (num > 0) {
        let curr = val[i];
        if (curr <= num) {
            res += hash[curr];
            num -= curr;
        }
        else
            i++;
    }
    return res;
};


console.log(intToRoman(234));