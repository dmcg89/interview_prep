def two_sum(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  required = {}
  for i in range(len(nums)):
      if target - nums[i] in required:
        return [required[target - nums[i]],i]
      else:
        required[nums[i]]=i

a=[5, 3, 6, 8, 2, 4, 7]
t=10
two_sum(a, t)