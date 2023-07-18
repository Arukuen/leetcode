def plusOne(digits: list[int]) -> list[int]:
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 9:
            return [*digits[:i], digits[i]+1, *[0]*(len(digits)-(i+1))]
        elif i == 0:
            return [1, *[0]*(len(digits))]
        
print(plusOne([1,2,3]))
