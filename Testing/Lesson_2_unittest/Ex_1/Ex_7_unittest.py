def first_last6(nums):
    if not nums:
        raise ValueError('The length of the list must be at least 1')
    if not all(isinstance(num, int) for num in nums):
        raise TypeError('The list must contain only integers')
    if nums[0] != 6 and nums[-1] != 6:
        return False
    return True

