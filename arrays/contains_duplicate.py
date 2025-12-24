class Solution:
    def hasDuplicate(self, nums):
        # Set to store numbers we have already seen
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
