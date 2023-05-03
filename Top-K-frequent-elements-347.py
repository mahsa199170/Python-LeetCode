class Solution(object):
    def topKFrequent(self, nums, k):
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] = 1

        freq = [[] for i in range(len(nums)+1)]

        for key,value in dict.items():
            freq[value].append(key)

        result = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result