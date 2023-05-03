class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        s = s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()

        dict = {}

        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for j in t:
            if j in dict:
                dict[j] -= 1
            else:
                dict[j] = 1

        for value in dict.values():
            if value != 0:
                return False
        return True
