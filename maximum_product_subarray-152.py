

class Solution(object):
    def maxProduct(self, nums):
        my_max = my_min = res = nums[0]

        for num in nums[1:]:
            curr_max = max(num, my_max * num, my_min * num)
            curr_min = min(num, my_max * num, my_min * num)

            my_max = curr_max
            my_min = curr_min

            res = max(my_max,res)

        return res



# time complexity: o(n)

# pace complexity: o(1)