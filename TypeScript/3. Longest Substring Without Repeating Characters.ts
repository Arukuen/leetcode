function lengthOfLongestSubstring(s: string): number {
    let hash = new Set();
    let l = 0;
    let output = 0;
    for (let i = 0; i < s.length; i++) {
        while (hash.has(s[i])) {
            hash.delete(s[l]);
            l++;
        }
        hash.add(s[i]);
        output = Math.max(output, hash.size);
    }
    return output;
};

console.log(lengthOfLongestSubstring("dvdf"));