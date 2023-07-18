def twoSum(self, nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i,x in enumerate(nums):
        subtracted = target - x
        if subtracted in hashmap:
            return [i, hashmap[subtracted]]
        hashmap[x] = i