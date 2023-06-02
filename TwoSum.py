# One pass Hash Table
# Also can be done using Two-Pass Hash Table or Brute Force
# Brute Force will result into O(n^2) Time complexity while other have O(n) only.

def TwoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return i, hashmap[complement]
        hashmap[nums[i]] = i


print(TwoSum([1, 7, 5, 2], 9))
