def removeElement(nums, val):
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
        j += 1
    return i


print(removeElement([4, 5], 4))
