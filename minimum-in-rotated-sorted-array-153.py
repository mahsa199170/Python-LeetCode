class Solution(object):
    def findMin(self, nums):

        res = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res


# time complexity: The time complexity  is O(logn) since we are using binary search to
# find the minimum element in the given rotated sorted array.

# pace complexity: o(1)