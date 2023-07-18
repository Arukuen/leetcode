export {};

function isPalindrome(x: number): boolean {
    // Negative is always non palindrome due to the sign
    if (x < 0) return false;

    // Getting the length without string conversion
    let length = Math.floor(Math.log10(x)) + 1;
    // Only loop half a length of times
    let loopLength = Math.floor(length / 2);

    for (let i = 0; i < loopLength; i++) {
        // ---- Extraction -----
        // Get left digit by floor division
        let left = Math.floor(x / (10**(length - 1)));
        // Get right digit by modulo
        let right = x % 10;
        
        if (left !== right) return false;

        // ---- Pruning -----
        // Prune left
        x = x % (10**(length - 1));
        // Prune right
        x =  Math.floor(x / 10);
        length -= 2;
    }
    
    return true;
};

console.log(isPalindrome(10));