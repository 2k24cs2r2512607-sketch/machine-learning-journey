def search(nums, target):
    nums.sort()
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
nums = [3, 4, 3, 2, 4, 6, 5]
target = 3
print(search(nums, target))
