class Solution:
    def findClosestNumber(self, nums):
        closest = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            if abs(x) < abs(closest) or (abs(x) == abs(closest) and x > closest):
                closest = x
        return closest
