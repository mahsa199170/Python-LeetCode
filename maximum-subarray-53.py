# previous subarray cannot be negative, dynamic programming: compute max sum for each prefix.

'''Kdane's Algorithm'''

"""sliding window"""
# 1. create a variable to hold the max sum
# 2. create a variable to hold the current sum
# 3. iterate through the list
# 4. if the current sum is less than 0, set it to 0
# 5. add the current number to the current sum
# 6. if the current sum is greater than the max sum, set the max sum to the current sum
# 7. return the max sum


class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0

        max_sum = nums[0]
        current_sum = 0

        for num in nums:

            if current_sum < 0:
                current_sum = 0

            current_sum += num
            max_sum = max(current_sum, max_sum)

        return max_sum



# time complexity is o(n)
# space complexity is