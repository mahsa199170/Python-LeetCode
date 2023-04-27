
nums = [-1,0,3,5,9,12]
target = 9

# Output: 4
# Explanation: 9 exists in nums and its index is 4


class Solution(object):
    def search(self, nums, target):

        i,j = 0,len(nums) - 1

        while i <= j :

            m = (i + j) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                i = m + 1
            else:
                j = m - 1

        return -1


# Time complexity of binary search : O(logn) cause evey time we are eliminating half of the possibilities




# ********************************************
# NOTE:
# There is a little bug here, infact this bug technically does not exist in python, cause python integeres are unbounded,
# they can pretty much be infinitely large, but in most languages such as java or c++ we might encounter
# an overflow, cause suppose if we had a very large input array and then the two of our pointers (i and j)
# were very close to 32-bit integer max which is something like 2^32, suppose they were both close to that
# then adding them together would possibly overflow and then we would get the wrong result fo rthe value
# not m
# so there is a way to hit that, and we can still calculate the mid by using our pointers ( i and j)
# without adding them together.
#
# we can get teh distance between them (i-j) and then dividing that by 2 ((i-j)//2) and
# this will give us half of the distance between them and we can take that and add it to the left index, cause
# if we have half of the distance between i and j, and i is the left index, and byadding this together we are
# getting the midway.
# this will never overflow
# ********************************************