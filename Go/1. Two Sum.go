package main

import "fmt"

func twoSum(nums []int, target int) []int {
	var hashTable = make(map[int]int)
	for i := 0; i < len(nums); i++ {
		subtracted := target - nums[i]
		if val, ok := hashTable[subtracted]; ok {
			return []int{val, i}
		}
		hashTable[nums[i]] = i
	}
	return []int{0, 0}
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	fmt.Println(twoSum(nums, target))
}
