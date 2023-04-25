
# first appraoch

# time complexity: O( m * n)
# space complexity: O(n)

class Solution(object):
    def groupAnagrams(self, strs):

        dict = defaultdict(list)

        for s in strs:
            count= [0] * 26
            for c in s:
                count[ord(c)- ord("a")] += 1
            dict[tuple(count)].append(s)
        return dict.values()

# -------------------------------------------------------------------------

# second approach

# on way to check if two strings are anagram is to sort them and check if they are the same,

# the time complexity is: O(m * nlogn) where n is the
# length of each string and nlogn is the time takes to sort each of the string,
# and we have to do it m times, m is the length of the whole array,
# space complexity = O(n)


class Solution(object):
    def groupAnagrams(self, strs):

        dict = defaultdict(list)

        for s in strs:
            new_s = "".join(sorted(s))
            if new_s in dict:
                dict[new_s].append(s)
            else:
                dict[new_s] = [s]

        return dict.values()
