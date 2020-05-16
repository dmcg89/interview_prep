def combsum (arr, targ):
  solutions = []
  combs = {}
  for elem in arr:
    nums = []
    nums.append(elem)
    print(nums, targ)
    while sum(nums) <= targ:
      combs[sum(nums)] = nums
      print(combs)
      print(targ-sum(nums))
      if (targ-sum(nums)) in combs:
      # if combs[(targ-sum(nums))]:
        print('here')
        # solutions.append(nums.append(targ-sum(nums)))
        print(nums)
        solutions.append(nums)
      nums.append(elem)
  return solutions

arr = [2,3,5]
# print(combsum(candidates, 8))

def combsum2 (arr, target):
  ans = []
  cands = sorted(arr)

  def dp(rem, sol, indx):
    if rem == 0: ans.append(sol)
    for i in range(indx, len(cands)):
      if cands[i] > rem: break
      dp(rem - cands[i], sol + [cands[i]], i)
  dp(rem = target, sol=[], indx=0)
  return ans

print(combsum2(arr, 8))
