
function romanToInt(s: string): number {
    let hash: { [key:string]: number } = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    };
    let roman = s.split('').reverse();
    let curr_max = 0;
    let res = 0;
    
    for (let i=0; i < roman.length; i++) {
        let curr = hash[roman[i]];
        if (curr >= curr_max) {
            res += curr;
            curr_max = curr;
        }
        else
            res -= curr;
    }
    return res;
};

console.log(romanToInt('MCMXCIV'));