function isAnagram(s: string, t: string): boolean {
    const hashS: {[key: string]: number} = {};
    const hashT: {[key: string]: number} = {};
    
    if (s.length !== t.length)
        return false;

    for (let i = 0; i < s.length; i++) {
        if (!(s[i] in hashS)) hashS[s[i]] = 1;
        else hashS[s[i]] += 1;
        
        if (!(t[i] in hashT)) hashT[t[i]] = 1;
        else hashT[t[i]] += 1;
    }

    for (const key in hashS) {
        if (hashS[key] !== hashT[key]) {
            return false;
        }
    }
    
    return true;
};

console.log(isAnagram("anagram", "nagaram"))