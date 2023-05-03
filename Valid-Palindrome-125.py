# solution 1: one way is to use isalnum built-in function

class Solution(object):
    def isPalindrome(self, s):

        i = 0
        j = len(s)-1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i].lower()!= s[j].lower():
                return False
            i+= 1
            j -=1
        return True




# solution 2 : one way is to use regular expression

class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[\W_]', '', s).lower()
        return s == s[::-1]


# one way is to create alphanum function(using ASCII  codes) then use it

s = "A man, a plan, a canal: Panama"



def alphanum(c):

    return (
        ord("A") <= ord(c) <= ord("Z") or
        ord("a") <= ord(c) <= ord("z") or
        ord("0") <= ord(c) <= ord("9")
    )



def palindrom(s):

    i = 0
    j = len(s) - 1

    while i < j:
        while i < j and not alphanum(s[i]):
            i +=1
        while i < j and not alphanum(s[j]):
            j -=1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True

print(palindrom(s))


