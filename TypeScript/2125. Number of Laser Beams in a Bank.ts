function numberOfBeams(bank: string[]): number {
    let lasers = 0;
    let prev = 0;
    for(let row of bank) {
        let len = row.split('').filter(l => l ==='1').length
        if (!len)
            continue;
        lasers += prev * len
        prev = len
    }
    return lasers;
};

console.log(numberOfBeams(["011001","000000","010100","001000"]))