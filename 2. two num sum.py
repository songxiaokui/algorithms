# Python
# O(n)
class Solution:
    def twoSum(self, nums: list, target: int) -> list[int]:
        hash_map = dict()
        for index, value in enumerate(nums):
            if target - value in hash_map.keys():
                return [hash_map[target-value], index]
            hash_map[value] = index
        return []


# Go
# O(n)
"""
func twoSum(nums []int, target int) []int {
    hash_map := make(map[int]int)
    result := []int{}
    for index, value :=range nums {
        if v,ok := hash_map[target-value]; ok {
            result = append(result, v)
            result = append(result, index)
            goto Label
        }
        hash_map[value] = index
    }
    Label:
    return result
}
"""

# O(n^2)
# 双循环
if __name__ == '__main__':
    a = Solution()
    print(a.twoSum(nums=[1, 3, 6, 5, 4], target=4))
