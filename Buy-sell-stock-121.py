class Solution(object):
    def maxProfit(self, prices):

        l, r = 0, 1
        max_price = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                res = prices[r] - prices[l]
                max_price = max(max_price, res)
            else:
                l = r
            r += 1
        return max_price


# Space complexity = O(1) , we used just couple of pointers and no arrays
# Time complexity = O(n), it is a linear solution and we are not doing any brute force