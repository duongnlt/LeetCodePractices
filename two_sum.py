def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    diff = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in diff:
            return [i, diff[temp]]
        else:
            diff[nums[i]] = i


a = [1, 7, 8, 10]
print(twoSum(a, 9))

        