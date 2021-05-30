class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, val in enumerate(nums):
            hashmap[val] = index
        for fst, val in enumerate(nums):
            sec = hashmap.get(target-val)
            if sec is not None and sec != fst:
                return [fst, sec]


sln = Solution()

result = sln.twoSum([2, 7, 11, 15], 26)

print(result)

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, data in enumerate(nums):
            hashmap[data] = i
        for i, data in enumerate(nums):
            j = hashmap.get(target-data)
            if j is not None and i != j:
                return [i, j]
"""