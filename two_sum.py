class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store numbers we have seen so far
        # Key   -> number value
        # Value -> index of that number
        seen = {}

        # Loop through the list once
        for i in range(len(nums)):
            # Current number
            current = nums[i]

            # The number we need to reach the target
            needed = target - current

            # Check if the needed number has already been seen
            if needed in seen:
                # If yes, return the index of the current number
                # and the index of the needed number
                return [seen[needed], i]

            # Otherwise, store the current number with its index
            seen[current] = i
