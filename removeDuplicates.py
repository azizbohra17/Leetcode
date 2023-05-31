def removeDuplicates(nums) -> int:
    # k_bar = 0
    # temp = 1
    # for i in range(1,len(nums)):
    #
    #     if nums[temp] == nums[i-1]:
    #         nums.remove(nums[i])
    #         nums.append('_')
    #         k_bar += 1
    #         temp = i + 1
    # k = len(nums) - k_bar
    size = len(nums)
    insertIndex = 1
    for i in range(1, size):
        # Found unique element
        if nums[i - 1] != nums[i]:
            # Updating insertIndex in our main array
            nums[insertIndex] = nums[i]
            # Incrementing insertIndex count by 1
            insertIndex = insertIndex + 1
    return insertIndex



print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
