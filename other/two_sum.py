def two_sum(arr, t):
    for i in arr:
        for j in arr:
            if i + j == t:
                return i, j

# we have two arrays
# find 2 elems whose sum is closest to target

# assume positive integers
# assume no duplicates

def two_sum_two(arr1, arr2, t):
    nums = ()
    for i in arr1:
        for j in arr2:
            if nums == (): nums =  (i,j)
            if abs(i + j - t) < abs(nums[0] + nums[1] - t):
                nums = (i,j)
    return nums\