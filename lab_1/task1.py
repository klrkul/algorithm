class Solution(object):
    def twoSum(self, nums, target):
        idx_nums = []
        for i in range(len(nums)):
            idx_nums.append([nums[i], i])
        idx_nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            curr = idx_nums[left][0] + idx_nums[right][0]
            if curr == target:
                return [idx_nums[left][1], idx_nums[right][1]]
            elif curr < target:
                left +=1
            else:
                right -=1
        return None